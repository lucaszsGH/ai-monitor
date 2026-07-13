const params = new URLSearchParams(location.search);
const requestedLanguage = params.get("lang");
const language = requestedLanguage === "zh" || requestedLanguage === "en"
  ? requestedLanguage
  : /^zh\b/i.test(navigator.language || "") ? "zh" : "en";
const page = ["now", "sessions", "usage"].includes(params.get("page")) ? params.get("page") : "now";

const TEXT = {
  zh: {
    appLabel: "DeepWheel AI Monitor · AI 编程状态副屏", navLabel: "视图", switchLanguage: "Switch to English",
    official: "官方", local: "本机", adapter: "适配器", manual: "手动", mock: "模拟", unavailableSource: "未接入",
    waiting: "等待你", blocked: "有卡点", error: "异常", working: "执行中", review: "待验收", completed: "已完成", idle: "暂停", unavailable: "不可用",
    demoMode: "模拟数据", privateMode: "私人预览", liveMode: "已同步", noDataMode: "数据不可用",
    fallback: "未接入", unknown: "未知", unknownTime: "时间未知", noAction: "暂无动作摘要",
    handedOff: "已交接", critical: "临界", healthy: "健康", unsupported: "暂不支持", notProvided: "未提供", sessions: "个会话", needsYou: "等待你",
    noSession: "暂无会话摘要", moreSessions: "另外", allSessions: "已显示全部会话",
    usagePeriod: "用量周期", used: "已用", remaining: "剩余", resetUnknown: "重置未知", usageAria: "用量已用",
    sort: "排序：等待你 → 卡点 → 执行中 → 待验收 → 最近活跃",
    ample: "充足", normal: "正常", low: "偏低", criticalQuota: "紧急", overallUsed: "整体已用", fiveHourWindow: "5 小时窗口", today: "今日消耗", recording: "记录中", dataSource: "数据来源", recentSeven: "近 7 日用量", dailyRecord: "每日消耗 · 示例记录",
    fullScreen: "全屏：分享 → 添加到主屏幕", demoTag: "模拟状态 · Demo", privateTag: "私人预览 · 未接入", liveTag: "本机摘要", noActionNeeded: "当前没有需要处理的动作",
    summaryOnly: "只显示摘要，不读取聊天全文", sourceFirst: "官方值优先 · 不抓 Cookie", contextNote: "Context 仅表示单个会话健康", lastSync: "最后同步",
    deviceCheck: "设备检查", close: "关闭", check: "检查", safe: "安全区 T/R/B/L", overflow: "溢出 X/Y", homeMode: "主屏模式", yes: "是", no: "否",
  },
  en: {
    appLabel: "DeepWheel AI Monitor · AI coding status screen", navLabel: "Views", switchLanguage: "切换到中文",
    official: "Official", local: "Local", adapter: "Adapter", manual: "Manual", mock: "Demo", unavailableSource: "Unavailable",
    waiting: "Needs you", blocked: "Blocked", error: "Error", working: "Working", review: "Review", completed: "Complete", idle: "Paused", unavailable: "Unavailable",
    demoMode: "Demo data", privateMode: "Private preview", liveMode: "Synced", noDataMode: "Data unavailable",
    fallback: "Unavailable", unknown: "Unknown", unknownTime: "Time unknown", noAction: "No action summary",
    handedOff: "Handed off", critical: "Critical", healthy: "Healthy", unsupported: "Unsupported", notProvided: "Not provided", sessions: "sessions", needsYou: "needs you",
    noSession: "No session summary", moreSessions: "more sessions", allSessions: "All sessions shown",
    usagePeriod: "Usage period", used: "Used", remaining: "Remaining", resetUnknown: "Reset unknown", usageAria: "usage used",
    sort: "Order: needs you → blocked → working → review → recent",
    ample: "Ample", normal: "Normal", low: "Low", criticalQuota: "Urgent", overallUsed: "Overall used", fiveHourWindow: "5-hour window", today: "Today", recording: "Recording", dataSource: "Data source", recentSeven: "Last 7 days", dailyRecord: "Daily usage · demo record",
    fullScreen: "Full screen: Share → Add to Home Screen", demoTag: "Synthetic status · Demo", privateTag: "Private preview · Unavailable", liveTag: "Local summary", noActionNeeded: "No action needs your attention",
    summaryOnly: "Summaries only · no full chat history", sourceFirst: "Official values first · no cookies", contextNote: "Context is single-session health only", lastSync: "Last sync",
    deviceCheck: "Device check", close: "Close", check: "CHECK", safe: "Safe T/R/B/L", overflow: "Overflow X/Y", homeMode: "Home Screen", yes: "Yes", no: "No",
  },
};
const t = TEXT[language];
const SOURCE_LABELS = { official: t.official, local: t.local, adapter: t.adapter, manual: t.manual, mock: t.mock, unavailable: t.unavailableSource };
const STATE_LABELS = { waiting: t.waiting, blocked: t.blocked, error: t.error, working: t.working, review: t.review, completed: t.completed, idle: t.idle, unavailable: t.unavailable };
const ORDER = { waiting: 0, blocked: 1, error: 1, working: 2, review: 3, completed: 4, idle: 5, unavailable: 6 };

document.documentElement.lang = language === "zh" ? "zh-CN" : "en";
document.querySelector("#app").setAttribute("aria-label", t.appLabel);
document.documentElement.classList.toggle(
  "is-standalone",
  Boolean(window.navigator.standalone) || matchMedia("(display-mode: standalone)").matches || params.get("standalone") === "1",
);
const safeParam = params.get("safe");
const safe = safeParam === null ? Number.NaN : Number(safeParam);
if (Number.isFinite(safe) && safe >= 0 && safe <= 96) {
  document.documentElement.style.setProperty("--safe-left", `${safe}px`);
  document.documentElement.style.setProperty("--safe-right", `${safe}px`);
}

function usageState(remaining) {
  if (!Number.isFinite(remaining)) return { id: "unknown", label: t.unavailableSource };
  if (remaining >= 70) return { id: "ample", label: t.ample };
  if (remaining >= 50) return { id: "normal", label: t.normal };
  if (remaining >= 30) return { id: "low", label: t.low };
  return { id: "critical", label: t.criticalQuota };
}

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
}

function field(object, key) {
  if (language === "en" && object?.[`${key}_en`] !== undefined) return object[`${key}_en`];
  return object?.[key];
}

function display(value, fallback = t.fallback) {
  return value === null || value === undefined || value === "" ? fallback : escapeHtml(value);
}

function percent(value) {
  return Number.isFinite(value) ? `${Math.max(0, Math.min(100, value))}%` : t.fallback;
}

function formatTime(value) {
  const date = new Date(value);
  return Number.isNaN(date.valueOf()) ? t.unknownTime : date.toLocaleTimeString(language === "zh" ? "zh-CN" : "en-US", { hour: "2-digit", minute: "2-digit" });
}

function urlFor(nextPage = page, changes = {}) {
  const query = new URLSearchParams(location.search);
  query.set("page", nextPage);
  query.set("lang", changes.lang || language);
  Object.entries(changes).forEach(([key, value]) => {
    if (key === "lang") return;
    if (value === null) query.delete(key); else query.set(key, value);
  });
  return `?${query.toString()}`;
}

function brand(provider) {
  const monogram = (provider.monogram || field(provider, "label") || "AI").slice(0, 2).toUpperCase();
  const icon = typeof provider.icon === "string" && /^provider-icons\/[A-Za-z0-9._-]+$/.test(provider.icon) ? provider.icon : null;
  const mark = icon ? `<img class="provider-mark provider-image" src="${escapeHtml(icon)}" alt="">` : `<span class="provider-mark mark-${escapeHtml(provider.id)}" aria-hidden="true">${escapeHtml(monogram)}</span>`;
  return `<div class="provider-id">${mark}<div><small>${display(field(provider, "owner"), "AI PROVIDER")}</small><h2>${display(field(provider, "label"))}</h2></div></div>`;
}

function header(data) {
  const pages = [["now", "NOW"], ["sessions", "SESSIONS"], ["usage", "USAGE"]];
  const modeLabel = data.screen?.mode === "demo" ? t.demoMode : data.screen?.mode === "private-preview" ? t.privateMode : data.screen?.mode === "live" ? t.liveMode : t.noDataMode;
  const nextLanguage = language === "zh" ? "en" : "zh";
  return `<header class="topbar">
    <div class="dw-lockup"><span class="dw-dot" aria-hidden="true"></span><span>DEEPWHEEL</span><b>AI MONITOR</b></div>
    <nav aria-label="${t.navLabel}">${pages.map(([id, label]) => `<a class="${page === id ? "active" : ""}" href="${urlFor(id)}">${label}</a>`).join("")}</nav>
    <div class="top-actions"><a class="language-switch" href="${urlFor(page, { lang: nextLanguage })}" aria-label="${t.switchLanguage}">${language === "zh" ? "EN" : "中"}</a><div class="sync"><span class="sync-dot"></span><span>${modeLabel}</span><time>${formatTime(data.updated_at)}</time></div></div>
  </header>`;
}

function sessionRow(session) {
  const state = session.state || "unavailable";
  const context = session.context_health || {};
  const contextText = context.handoff_ready ? `${t.handedOff} ${percent(context.used_percent)}`
    : context.level === "critical" ? `${t.critical} ${percent(context.used_percent)}`
    : context.level === "healthy" ? `${t.healthy} ${percent(context.used_percent)}`
    : context.source === "unsupported" ? t.unsupported : t.notProvided;
  const contextClass = context.handoff_ready ? "handoff" : context.level === "critical" ? "risk" : context.level === "healthy" ? "healthy" : "unknown";
  return `<div class="session-row ${escapeHtml(state)}">
    <span class="session-state">${display(field(session, "state_label"), STATE_LABELS[state] || t.unknown)}</span>
    <div class="session-copy"><b>${display(field(session, "label"))}</b><span>${display(field(session, "current_action"), t.noAction)}</span></div>
    <div class="session-meta ${contextClass}"><b>${contextText}</b><span>${display(field(session, "updated_label"), t.unknownTime)}</span></div>
  </div>`;
}

function sortedSessions(provider) {
  return [...(provider.sessions || [])].sort((a, b) => {
    const aa = a.attention?.required ? -1 : (ORDER[a.state] ?? 99);
    const bb = b.attention?.required ? -1 : (ORDER[b.state] ?? 99);
    const ac = Number.isFinite(a.context_health?.used_percent) ? 0 : 1;
    const bc = Number.isFinite(b.context_health?.used_percent) ? 0 : 1;
    return aa - bb || ac - bc || String(b.updated_at || "").localeCompare(String(a.updated_at || ""));
  });
}

function usageStrip(provider) {
  const usage = provider.usage || {};
  const quickUsed = Number.isFinite(usage.quick_used_percent) ? usage.quick_used_percent : usage.used_percent;
  const quickRemaining = Number.isFinite(usage.quick_remaining_percent) ? usage.quick_remaining_percent : usage.remaining_percent;
  const used = Number.isFinite(quickUsed) ? Math.max(0, Math.min(100, quickUsed)) : 0;
  const remaining = Number.isFinite(quickRemaining) ? quickRemaining : null;
  const state = usageState(remaining);
  return `<div class="usage-strip usage-${state.id}">
    <div class="usage-copy"><small>${display(field(usage, "quick_period_label") || field(usage, "period_label"), t.usagePeriod)}</small><b>${t.used} ${percent(quickUsed)}</b></div>
    <div class="usage-bar" role="progressbar" aria-label="${display(field(provider, "label"))} ${t.usageAria}" aria-valuenow="${used}" aria-valuemin="0" aria-valuemax="100"><i style="width:${used}%"></i></div>
    <div class="usage-meta"><strong>${state.label} · ${t.remaining} ${percent(remaining)}</strong><span>${display(field(usage, "quick_reset_label") || field(usage, "reset_label"), t.resetUnknown)}</span></div>
  </div>`;
}

function nowCard(provider) {
  const sessions = sortedSessions(provider);
  const attention = sessions.filter((item) => item.attention?.required).length;
  return `<article class="provider-card">
    <div class="provider-head">${brand(provider)}<div class="provider-count"><b>${sessions.length}</b><span>${t.sessions}</span><em>${attention} ${t.needsYou}</em></div></div>
    <div class="session-list">${sessions.slice(0, 2).map(sessionRow).join("") || `<p class="empty">${t.noSession}</p>`}</div>
    <div class="more-sessions">${sessions.length > 2 ? `+ ${t.moreSessions} ${sessions.length - 2}` : t.allSessions}</div>
    ${usageStrip(provider)}
  </article>`;
}

function sessionsCard(provider) {
  const sessions = sortedSessions(provider);
  const attention = sessions.filter((item) => item.attention?.required).length;
  return `<article class="sessions-panel"><div class="provider-head">${brand(provider)}<div class="provider-count"><b>${sessions.length}</b><span>${t.sessions}</span><em>${attention} ${t.needsYou}</em></div></div>
    <div class="sessions-all">${sessions.slice(0, 4).map(sessionRow).join("") || `<p class="empty">${t.noSession}</p>`}</div>
    <div class="sessions-foot">${t.sort}</div></article>`;
}

function usageCard(provider) {
  const usage = provider.usage || {};
  const remaining = usage.remaining_percent;
  const state = usageState(remaining);
  const trend = Array.isArray(usage.trend) ? usage.trend.slice(-7) : [];
  const trendLabels = Array.isArray(usage.trend_labels) ? usage.trend_labels.slice(-7) : [];
  const fallbackLabels = language === "zh" ? ["一", "二", "三", "四", "五", "六", "日"] : ["M", "T", "W", "T", "F", "S", "S"];
  const bars = trend.map((value, index) => {
    const today = index === trend.length - 1;
    const tone = today ? "today" : `tone-${index % 3}`;
    const available = Number.isFinite(value);
    const height = available ? Math.max(4, Math.min(100, value)) : 4;
    return `<div class="pressure-item ${tone} ${available ? "" : "empty-bar"}" style="--bar:${height}%"><span>${available ? percent(value) : "—"}</span><i></i><b>${display(field({ value: trendLabels[index] }, "value"), fallbackLabels[index] || "")}</b></div>`;
  }).join("");
  const hasQuick = Number.isFinite(usage.quick_remaining_percent);
  const middleLabel = hasQuick ? t.fiveHourWindow : t.today;
  const middleValue = hasQuick ? `${t.remaining} ${percent(usage.quick_remaining_percent)}` : Number.isFinite(usage.daily_used_percent) ? percent(usage.daily_used_percent) : t.recording;
  const middleState = hasQuick ? usageState(usage.quick_remaining_percent).id : "data";
  return `<article class="usage-panel usage-${state.id}">
    <div class="provider-head">${brand(provider)}<div class="source-badge">${display(SOURCE_LABELS[usage.source] || usage.source)}</div></div>
    <div class="usage-main">
      <div class="usage-hero"><small>${display(field(usage, "period_label"), t.usagePeriod)}</small><div><b>${Number.isFinite(remaining) ? remaining : "—"}</b><sup>${Number.isFinite(remaining) ? "%" : ""}</sup></div><span>${t.remaining} · ${display(field(usage, "reset_label"), t.resetUnknown)}</span></div>
      <div class="pressure"><div class="pressure-head"><b>${t.recentSeven}</b><span>${t.dailyRecord}</span></div><div class="pressure-bars">${bars}</div></div>
    </div>
    <div class="usage-detail"><div><small>${t.overallUsed}</small><b>${percent(usage.used_percent)}</b></div><div class="detail-${middleState}"><small>${middleLabel}</small><b>${middleValue}</b></div><div><small>${t.dataSource}</small><b>${display(SOURCE_LABELS[usage.source] || usage.source)}</b></div></div>
  </article>`;
}

function footer(data, providers) {
  if (page === "now") {
    const needs = providers.flatMap((provider) => sortedSessions(provider).filter((item) => item.attention?.required));
    const standalone = Boolean(window.navigator.standalone) || matchMedia("(display-mode: standalone)").matches;
    const iPhone = /iPhone|iPad|iPod/i.test(navigator.userAgent);
    const modeTag = iPhone && !standalone ? t.fullScreen : data.screen?.mode === "demo" ? t.demoTag : data.screen?.mode === "private-preview" ? t.privateTag : data.screen?.mode === "live" ? t.liveTag : t.noDataMode;
    return `<footer class="alert"><span class="alert-count">${needs.length}</span><div><small>NEEDS YOU</small><b>${needs.length ? needs.slice(0, 2).map((item) => display(field(item, "label"))).join(" · ") : t.noActionNeeded}</b></div><span class="mode-tag">${modeTag}</span></footer>`;
  }
  const legend = language === "zh"
    ? `<span class="quota-legend"><i class="ample">✓ <b>充足</b> ≥70%</i><i class="normal">● <b>正常</b> 50–69%</i><i class="low">! <b>偏低</b> 30–49%</i><i class="critical">! <b>紧急</b> &lt;30%</i></span>`
    : `<span class="quota-legend"><i class="ample">✓ <b>AMPLE</b> ≥70%</i><i class="normal">● <b>NORMAL</b> 50–69%</i><i class="low">! <b>LOW</b> 30–49%</i><i class="critical">! <b>URGENT</b> &lt;30%</i></span>`;
  return `<footer class="foot"><span>${page === "sessions" ? t.summaryOnly : t.sourceFirst}</span>${page === "sessions" ? `<b>${t.contextNote}</b>` : legend}<time>${t.lastSync} ${formatTime(data.updated_at)}</time></footer>`;
}

function render(data) {
  const providers = (data.providers || []).slice(0, 2);
  while (providers.length < 2) providers.push({ id: `empty-${providers.length}`, label: t.fallback, owner: "PROVIDER", monogram: "AI", sessions: [], usage: { source: "unavailable" } });
  const card = page === "sessions" ? sessionsCard : page === "usage" ? usageCard : nowCard;
  document.querySelector("#app").innerHTML = `${header(data)}<section class="peer-grid ${page}-grid">${providers.map(card).join("")}</section>${footer(data, providers)}`;
  requestAnimationFrame(() => {
    document.body.dataset.overflowX = String(document.documentElement.scrollWidth > innerWidth + 1);
    document.body.dataset.overflowY = String(document.documentElement.scrollHeight > innerHeight + 1);
    renderDeviceCheck();
  });
}

function renderDeviceCheck() {
  if (params.get("debug") !== "1" || document.querySelector("#device-check")) return;
  const probe = document.createElement("div");
  probe.className = "safe-probe";
  document.body.append(probe);
  const style = getComputedStyle(probe);
  const insets = [style.paddingTop, style.paddingRight, style.paddingBottom, style.paddingLeft];
  probe.remove();
  const landscape = innerWidth > innerHeight;
  const overflowX = document.documentElement.scrollWidth > innerWidth + 1;
  const overflowY = document.documentElement.scrollHeight > innerHeight + 1;
  const standalone = Boolean(window.navigator.standalone) || matchMedia("(display-mode: standalone)").matches;
  const passed = landscape && !overflowX && !overflowY;
  const panel = document.createElement("aside");
  panel.id = "device-check";
  panel.setAttribute("aria-label", t.deviceCheck);
  panel.innerHTML = `<div><b>${t.deviceCheck.toUpperCase()}</b><a href="${urlFor(page, { debug: null })}">${t.close}</a></div>
    <p class="${passed ? "pass" : "fail"}">${passed ? "PASS" : t.check} · ${innerWidth}×${innerHeight}</p>
    <p>${t.safe} · ${insets.join(" / ")}</p><p>${t.overflow} · ${overflowX} / ${overflowY}</p><p>${t.homeMode} · ${standalone ? t.yes : t.no}</p>`;
  document.body.append(panel);
}

fetch("status.example.json", { cache: "no-store" })
  .then((response) => { if (!response.ok) throw new Error("status unavailable"); return response.json(); })
  .then(render)
  .catch(() => render({ schema_version: "2.0", updated_at: null, screen: { mode: "unavailable" }, providers: [] }));
