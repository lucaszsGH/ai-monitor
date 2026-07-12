# 状态数据合同

## 目标

统一不同 Agent 的最小状态，不把平台差异、凭证或会话全文带进前端。

## 公共字段

```json
{
  "schema_version": "1.0",
  "updated_at": "2026-01-01T09:30:00+08:00",
  "screen": {
    "title": "AI Watchtower",
    "mode": "demo"
  },
  "agents": [
    {
      "id": "agent-a",
      "label": "Claude",
      "state": "working",
      "current_task": "Reviewing the plan",
      "context_window": {
        "used_percent": 42,
        "source": "mock"
      },
      "quota": {
        "remaining_percent": null,
        "resets_at": null,
        "source": "unavailable"
      },
      "work_context": {
        "objective": "Validate the information architecture",
        "next_action": "Return a review summary",
        "blocker": null,
        "verified_at": "2026-01-01T09:29:00+08:00"
      },
      "attention": {
        "required": false,
        "reason": null
      }
    }
  ]
}
```

## 合法状态

`idle | working | waiting | completed | error | unavailable`

## 字段规则

- 百分比范围为 0–100；来源必须是 `official | local | adapter | manual | mock | unavailable`。
- 不知道时使用 `null`，不得估算后伪装成官方值。
- `current_task`、`objective`、`next_action` 使用摘要，不放提示词或聊天原文。
- `blocker` 只写可操作卡点，不写敏感报错全文。
- `updated_at` 与 `verified_at` 分开：数据刷新不等于工作结论已核实。
- 前端不得接收凭证、Cookie、Authorization header、绝对路径或完整日志字段。

## 私人字段隔离

私人项目名、本机路径、内部决策和真实任务可以留在本机覆盖层，但不得写入公开模板、示例、测试、Issue、截图或仓库历史。

