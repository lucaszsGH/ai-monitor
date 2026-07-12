const stateLabels = {
  idle: "空闲",
  working: "工作中",
  waiting: "等待处理",
  completed: "已完成",
  error: "异常",
  unavailable: "不可用",
};

const stateSymbols = {
  idle: "·",
  working: "✓",
  waiting: "◷",
  completed: "✓",
  error: "!",
  unavailable: "–",
};

const sourceLabels = {
  official: "官方",
  local: "本机",
  adapter: "适配器",
  manual: "手动",
  mock: "模拟",
  unavailable: "不可用",
};

function percent(value) {
  return Number.isFinite(value) ? `${Math.max(0, Math.min(100, value))}%` : "—";
}

function setMeter(element, value) {
  const safe = Number.isFinite(value) ? Math.max(0, Math.min(100, value)) : 0;
  element.style.width = `${safe}%`;
}

function renderAgent(agent, index) {
  const template = document.querySelector("#agent-card-template");
  const fragment = template.content.cloneNode(true);
  const card = fragment.querySelector(".agent-card");
  card.dataset.agent = agent.id;
  card.dataset.state = agent.state;

  fragment.querySelector(".agent-provider").textContent = "AGENT STATUS";
  fragment.querySelector(".agent-label").textContent = agent.label;
  const badge = fragment.querySelector(".state-badge");
  const stateLabel = stateLabels[agent.state] ?? "未知";
  const stateSymbol = stateSymbols[agent.state] ?? "·";
  badge.textContent = `${stateSymbol} ${stateLabel}`;
  badge.dataset.state = agent.state;
  fragment.querySelector(".current-task").textContent = agent.current_task || "当前任务未提供";

  const context = agent.context_window ?? {};
  fragment.querySelector(".context-value").textContent = percent(context.used_percent);
  fragment.querySelector(".context-source").textContent = `来源：${sourceLabels[context.source] ?? "未知"}`;
  const gauge = fragment.querySelector(".context-gauge");
  const contextValue = Number.isFinite(context.used_percent)
    ? Math.max(0, Math.min(100, context.used_percent))
    : 0;
  const contextColor = contextValue >= 85
    ? "var(--dw-error)"
    : contextValue >= 70
      ? "var(--dw-warning)"
      : "var(--dw-success)";
  gauge.style.setProperty("--gauge-value", contextValue);
  gauge.style.setProperty("--context-color", contextColor);
  gauge.setAttribute("aria-label", `Context 已使用 ${percent(context.used_percent)}`);
  gauge.setAttribute("aria-valuenow", contextValue);

  const quota = agent.quota ?? {};
  fragment.querySelector(".quota-value").textContent = percent(quota.remaining_percent);
  fragment.querySelector(".quota-source").textContent = `来源：${sourceLabels[quota.source] ?? "未知"}`;
  const quotaMeter = fragment.querySelector(".quota-meter");
  const quotaTrack = quotaMeter.parentElement;
  const quotaValue = Number.isFinite(quota.remaining_percent)
    ? Math.max(0, Math.min(100, quota.remaining_percent))
    : 0;
  setMeter(quotaMeter, quota.remaining_percent);
  quotaTrack.setAttribute("aria-valuenow", quotaValue);
  quotaTrack.setAttribute("aria-label", `Quota 剩余 ${percent(quota.remaining_percent)}`);

  const work = agent.work_context ?? {};
  fragment.querySelector(".next-action").textContent = work.next_action || "下一步未提供";
  return fragment;
}

async function loadStatus() {
  const syncLabel = document.querySelector("#sync-label");
  syncLabel.textContent = "同步中";

  try {
    const response = await fetch("status.example.json", { cache: "no-store" });
    if (!response.ok) throw new Error("status unavailable");
    const data = await response.json();

    const grid = document.querySelector("#agent-grid");
    grid.replaceChildren(...data.agents.map(renderAgent));
    document.querySelector("#global-objective").textContent = data.global_objective || "当前目标未提供";

    const attention = data.agents.filter((agent) => agent.attention?.required);
    document.querySelector("#attention-message").textContent = attention.length
      ? `${attention.length} 个 Agent 需要你处理：${attention.map((agent) => agent.label).join("、")}`
      : "当前没有需要你处理的动作";

    const updated = new Date(data.updated_at);
    document.querySelector("#updated-at").textContent = Number.isNaN(updated.valueOf())
      ? "时间未知"
      : updated.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    syncLabel.textContent = "已同步";
  } catch {
    syncLabel.textContent = "连接中断";
    document.querySelector("#attention-message").textContent = "状态服务不可用，请检查本机服务后重试";
  }
}

document.querySelector("#refresh-button").addEventListener("click", loadStatus);
loadStatus();
