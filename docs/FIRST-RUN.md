# First Run: an iPhone landscape status screen in 10 minutes

Goal: complete one safe and reversible demo-data experience before connecting Claude, Codex, or any background service.

## Before you start

You need Python 3.10+, Safari, an iPhone X through iPhone 17 Pro Max, and a computer and phone on the same trusted Wi-Fi. You do not need an API key, provider login, Node.js, a plugin, or a public server.

## 1. Generate the demo

From the repository root:

```bash
python3 skills/lucas-deepwheel-ai-monitor/scripts/create_ai_monitor.py \
  --output ./ai-monitor-demo
```

Expect `CREATED` and `MODE: demo data only`. The generator refuses to overwrite a non-empty directory.

## 2. Validate before opening it

```bash
python3 skills/lucas-deepwheel-ai-monitor/scripts/validate_ai_monitor.py \
  ./ai-monitor-demo
```

Expected result: `CLEAN`.

## 3. Preview on the computer first

```bash
cd ai-monitor-demo
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765`. After NOW, SESSIONS, and USAGE render, stop the server with `Control+C`.

## 4. Confirm trusted-LAN access

This step exposes port `8765` to devices on the same local network. Use it only on a trusted home or office Wi-Fi, never with public port forwarding.

After confirming the boundary, run:

```bash
python3 -m http.server 8765 --bind 0.0.0.0
```

Find the computer's LAN address:

- macOS: `ipconfig getifaddr en0`, then try `en1` if needed;
- Windows: run `ipconfig` and find the current IPv4 Address;
- Linux: run `hostname -I`.

If the address is `192.168.1.20`, open `http://192.168.1.20:8765` on the iPhone. Do not use `127.0.0.1` on the phone.

## 5. Check landscape and Home Screen mode

1. Rotate the iPhone to landscape.
2. Open `http://COMPUTER-IP:8765/?debug=1`.
3. Confirm PASS and no horizontal or vertical overflow.
4. In Safari, choose Share → Add to Home Screen.
5. Enable Open as Web App when the option is available.
6. Launch AI Monitor from its Home Screen icon.
7. It follows the system language by default; use the compact `EN／中` control when you want to switch.

The black device base, safe-area guards, and full-screen viewport rules cover the landscape size range from iPhone X through 17 Pro Max. Automation does not replace a real-device check for notches, Dynamic Island, Display Zoom, or text settings.

## 6. Choose only one next layer

- Keep demo mode.
- Maintain a minimal status JSON manually.
- Review and authorize a read-only live-data adapter.
- Review and authorize private-network access separately.

Do not jump from demo mode to cookie scraping, full-transcript reading, or public exposure.

## 60-second recovery

| Symptom | Check first |
|---|---|
| Phone cannot connect | Same Wi-Fi, computer LAN IP, host firewall, guest-network isolation |
| Safari chrome remains visible | Add to Home Screen and launch from the icon |
| Notch or Dynamic Island overlaps content | Rotate, reload, and inspect `?debug=1` |
| Large empty area below the footer | Use the current starter with browser `100dvh` and Home Screen `100lvh` handling |
| Page stops after sleep | Wake the computer or restart the terminal server |
| Stop sharing | Press `Control+C` in the server terminal |

## First-success checklist

- [ ] Desktop demo opens.
- [ ] NOW, SESSIONS, and USAGE open on the landscape iPhone.
- [ ] `?debug=1` reports PASS.
- [ ] Home Screen mode removes Safari chrome.
- [ ] The notch or Dynamic Island does not cover text.
- [ ] The user knows the data is synthetic.
- [ ] The user knows how to stop the server.
