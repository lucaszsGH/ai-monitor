#!/usr/bin/env python3
"""Run a local Chrome layout smoke test across common phone landscape sizes."""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "skills" / "lucas-deepwheel-ai-watchtower" / "assets" / "starter"
SIZES = [
    (812, 375, 44, 21),  # iPhone X / XS / 11 Pro class
    (844, 390, 47, 21),  # iPhone 12 / 13 / 14 class
    (852, 393, 59, 21),  # iPhone 14 Pro / 15 Pro class
    (874, 402, 59, 21),  # intermediate modern viewport guard
    (896, 414, 44, 21),  # iPhone XR / XS Max / 11 / 11 Pro Max class
    (926, 428, 47, 21),  # iPhone 12 / 13 / 14 Pro Max class
    (932, 430, 59, 21),  # iPhone Plus / 15 Pro Max class
    (956, 440, 62, 21),  # iPhone 16 / 17 Pro Max physical 3x class
    (956, 440, None, None),  # default CSS obstruction guard, no query override
]
PAGES = ("now", "sessions", "usage")
LANGUAGES = ("zh", "en")
BROWSER_ENDPOINTS = (
    (812, 375, 44, 21),
    (956, 440, 62, 21),
)


def find_chrome(explicit: str | None) -> str | None:
    candidates = [
        explicit,
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    return None


def qa_page(
    font_scale: int,
    safe_side: int | None,
    safe_bottom: int | None,
    page: str,
    standalone: bool,
    language: str,
) -> str:
    safe_script = "" if safe_side is None else f"""
  doc.documentElement.style.setProperty('--safe-left', '{safe_side}px');
  doc.documentElement.style.setProperty('--safe-right', '{safe_side}px');
  doc.documentElement.style.setProperty('--safe-bottom', '{safe_bottom}px');"""
    query = f"?page={page}&amp;lang={language}" if safe_side is None else f"?page={page}&amp;lang={language}&amp;safe={safe_side}"
    if standalone:
        query += "&amp;standalone=1"
    return f"""<!doctype html>
<meta charset=\"utf-8\">
<style>html,body,iframe{{margin:0;width:100%;height:100%;border:0;overflow:hidden}}</style>
<script>
function measure(frame) {{
  const doc = frame.contentDocument;
  const win = frame.contentWindow;
  doc.documentElement.style.fontSize = '{font_scale}%';
{safe_script}
  const app = doc.querySelector('#app');
  const appRect = app.getBoundingClientRect();
  const overlaps = (left, right) => {{
    if (!left || !right) return false;
    const a = left.getBoundingClientRect();
    const b = right.getBoundingClientRect();
    return Math.min(a.right, b.right) - Math.max(a.left, b.left) > 1 &&
      Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > 1;
  }};
  const criticalPairs = [];
  const addPair = (name, left, right) => {{ if (overlaps(left, right)) criticalPairs.push(name); }};
  addPair('header-lockup-nav', doc.querySelector('.dw-lockup'), doc.querySelector('.topbar nav'));
  addPair('header-nav-actions', doc.querySelector('.topbar nav'), doc.querySelector('.top-actions, .sync'));
  doc.querySelectorAll('.provider-head').forEach((head, index) =>
    addPair(`provider-head-${{index}}`, head.querySelector('.provider-id'), head.querySelector('.provider-count, .source-badge'))
  );
  doc.querySelectorAll('.session-row').forEach((row, index) => {{
    addPair(`session-state-copy-${{index}}`, row.querySelector('.session-state'), row.querySelector('.session-copy'));
    addPair(`session-copy-meta-${{index}}`, row.querySelector('.session-copy'), row.querySelector('.session-meta'));
  }});
  doc.querySelectorAll('.usage-main').forEach((main, index) =>
    addPair(`usage-main-${{index}}`, main.querySelector('.usage-hero'), main.querySelector('.pressure'))
  );
  const unsafeText = [...doc.querySelectorAll('.usage-hero > span, .dw-lockup, .top-actions')]
    .filter((node) => node.scrollWidth > node.clientWidth + 1 && getComputedStyle(node).overflowX === 'visible')
    .map((node) => node.className || node.tagName);
  const payload = {{
    viewportWidth: win.innerWidth,
    viewportHeight: win.innerHeight,
    scrollWidth: doc.documentElement.scrollWidth,
    scrollHeight: doc.documentElement.scrollHeight,
    horizontalOverflow: doc.documentElement.scrollWidth > win.innerWidth + 1,
    verticalOverflow: doc.documentElement.scrollHeight > win.innerHeight + 1,
    appBottomGap: Math.round((win.innerHeight - appRect.bottom) * 100) / 100,
    standaloneClass: doc.documentElement.classList.contains('is-standalone'),
    criticalOverlap: criticalPairs,
    unsafeTextOverflow: unsafeText
  }};
  document.querySelector('#result').textContent = JSON.stringify(payload);
}}
</script>
<iframe id=\"target\" src=\"index.html{query}\" onload=\"measure(this)\"></iframe>
<output id=\"result\">pending</output>"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test common phone landscape viewports.")
    parser.add_argument("--chrome", help="Chrome or Chromium executable")
    parser.add_argument("--font-scale", type=int, default=100, choices=(100, 200))
    args = parser.parse_args()
    chrome = find_chrome(args.chrome)
    if not chrome:
        print("SKIP: Chrome or Chromium is unavailable")
        return 0

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        shutil.copytree(STARTER, root / "site")
        class QuietHandler(SimpleHTTPRequestHandler):
            def log_message(self, format: str, *values: object) -> None:
                return

        handler = lambda *a, **kw: QuietHandler(*a, directory=str(root / "site"), **kw)
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        port = server.server_port

        failures: list[str] = []
        try:
            cases = [(*case, True) for case in SIZES] + [(*case, False) for case in BROWSER_ENDPOINTS]
            for width, height, safe_side, safe_bottom, standalone in cases:
                for language in LANGUAGES:
                    for page in PAGES:
                        (root / "site" / "qa.html").write_text(
                            qa_page(args.font_scale, safe_side, safe_bottom, page, standalone, language),
                            encoding="utf-8",
                        )
                        command = [
                            chrome,
                            "--headless=new",
                            "--disable-gpu",
                            "--hide-scrollbars",
                            f"--window-size={width},{height}",
                            "--virtual-time-budget=1800",
                            "--dump-dom",
                            f"http://127.0.0.1:{port}/qa.html",
                        ]
                        result = subprocess.run(command, text=True, capture_output=True, check=False)
                        marker = '<output id="result">'
                        if result.returncode != 0 or marker not in result.stdout:
                            failures.append(f"{language}/{page} {width}x{height}: browser result unavailable")
                            continue
                        encoded = result.stdout.split(marker, 1)[1].split("</output>", 1)[0]
                        try:
                            payload = json.loads(html.unescape(encoded))
                        except json.JSONDecodeError:
                            failures.append(f"{language}/{page} {width}x{height}: measurement did not finish")
                            continue
                        horizontal = bool(payload["horizontalOverflow"])
                        vertical = bool(payload["verticalOverflow"])
                        bottom_gap = abs(float(payload["appBottomGap"]))
                        standalone_class = bool(payload["standaloneClass"])
                        critical_overlap = list(payload.get("criticalOverlap", []))
                        unsafe_text = list(payload.get("unsafeTextOverflow", []))
                        if horizontal or vertical or bottom_gap > 1 or critical_overlap or unsafe_text or (standalone and not standalone_class):
                            failures.append(
                                f"{language}/{page} {width}x{height}: horizontal={horizontal} vertical={vertical} "
                                f"bottom_gap={bottom_gap} standalone_class={standalone_class} "
                                f"critical_overlap={critical_overlap} unsafe_text={unsafe_text}"
                            )
                        else:
                            print(
                                f"PASS: {language}/{page} {width}x{height} mode={'standalone' if standalone else 'browser'} "
                                f"safe={'default' if safe_side is None else str(safe_side) + 'px'} "
                                f"font={args.font_scale}% bottom-gap={bottom_gap}px"
                            )
        finally:
            server.shutdown()
            server.server_close()

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("PASS: device matrix layout smoke test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
