# 多会话状态数据合同 v2.0

## 目标

统一多个 AI 工具、多个会话和账号级用量。前端只接收清洗后的摘要，不接触凭证、聊天全文或原始日志。

## 层级

```text
Provider（工具／账号）
├── Usage（账号级用量）
└── Sessions（多个会话）
    └── Context health（只属于单个会话）
```

核心规则：账号用量不能塞进会话 Context；多个会话的 Context 百分比不能相加。

## 最小 JSON

```json
{
  "schema_version": "2.0",
  "updated_at": "2026-01-01T09:30:00+08:00",
  "screen": { "title": "AI Monitor", "mode": "demo" },
  "providers": [
    {
      "id": "agent-a",
      "label": "Agent A",
      "owner": "AI Provider",
      "monogram": "A",
      "icon": null,
      "usage": {
        "scope": "provider_account",
        "period_label": "Current window",
        "used_percent": null,
        "remaining_percent": null,
        "reset_label": null,
        "today_label": null,
        "source": "unavailable",
        "verified_label": null,
        "trend": []
      },
      "sessions": [
        {
          "id": "opaque-local-id",
          "label": "Short user-authored title",
          "state": "working",
          "state_label": null,
          "current_action": "Sanitized one-line summary",
          "attention": { "required": false, "reason": null },
          "context_health": {
            "level": "healthy",
            "used_percent": null,
            "handoff_ready": false,
            "source": "manual"
          },
          "updated_at": "2026-01-01T09:29:00+08:00",
          "updated_label": "1 min"
        }
      ]
    }
  ]
}
```

## 枚举与排序

- 会话状态：`waiting | blocked | error | working | review | completed | idle | unavailable`。
- Context 健康：`healthy | critical | unknown`。
- 来源：`official | local | adapter | manual | mock | unavailable`。
- NOW 页排序：需要用户 → 卡点／异常 → 执行中 → 待验收 → 最近活跃。

## 不变量

- 未知值保持 `null`，界面显示“未接入”，不得猜测。
- `usage` 始终属于 Provider；`context_health` 始终属于 Session。
- `current_action` 只写一句经过清洗的动作摘要，不复制提示词或回复。
- `attention.reason` 只使用短原因，不复制敏感报错。
- 公开包只带中性标记和合成数据；第三方商标由使用者自行按品牌规则配置。
- `icon` 仅允许 `provider-icons/` 下的本地相对文件；公开示例必须保持 `null`，不得加载远程追踪图片。
- `usage.trend` 最多显示最近 7 个数值，只表示同一账号用量序列；不得混入不同周期或会话 Context。
- `state_label` 可在私人层覆盖状态中文文案，但不能改变底层 `state` 语义。
- 前端不得接收凭证、Cookie、Authorization header、完整路径、完整日志、聊天正文或客户资料。

## 适配器输出规则

每个适配器只写一个临时快照，再由校验器检查后替换前端状态文件。适配器失败时保留上一份合格快照，并把来源标成 `unavailable`；不得把原始输出直接传到浏览器。
