---
name: lucas-deepwheel-ai-monitor
description: "Use when a user wants to turn an iPhone or mobile browser into a landscape AI status screen for Claude Code, Codex, or adjacent agent CLIs. Guides capability preflight, privacy-safe data contracts, bilingual PWA generation, DeepWheel landscape UI, local-only deployment, context and quota separation, and release validation. Trigger for AI副屏, AI Monitor, 手机横屏驾驶舱, Claude/Codex状态屏, agent dashboard, PWA status monitor, usage/context dashboard. Do not expose credentials, full conversations, private project data, or open a remote-control surface without explicit confirmation."
---

# AI Monitor

定位：把手机横屏变成 Claude、Codex 等 AI Agent 的低打扰状态副屏。优先做安全、只读、局域网可用的 PWA；不要先做远程终端或完整聊天镜像。

## 什么时候使用

- 用户提到 AI 副屏、手机横屏驾驶舱、Claude/Codex 状态、Context 或额度看板；
- 用户想生成、审查或部署只读 Agent Dashboard；
- 用户提供现有网页、文件夹、JSON 或状态说明，希望改造成手机横屏界面；
- 用户需要把状态屏方法封装成可复用 Skill 或公开项目。

## 什么时候不要使用

- 用户只想查看单个平台官方额度页面；
- 用户要求绕过登录、抓取凭证或未经授权控制他人设备；
- 用户把状态屏当作完整远程终端，而没有独立威胁模型和动作确认；
- 目标只是普通数据看板，与 AI Agent 状态、手机副屏或工作连续性无关。

## 首先判断用户模式

先问自己：页面只给当前用户看，还是会交给团队、客户或公众？

- 用户自用：优先一眼看懂、少配置、少打扰、可恢复。
- 对外或团队：先锁终端用户、访问边界、信任结果和不可公开字段，再设计与部署。

用途不清时只问一句：这个状态屏只给你自己看，还是准备给团队或公众使用？

## 标准流程

按以下顺序推进，不跳层：

1. **对象**：确认设备、横竖屏、显示用途和是否只读。
2. **关系**：分清额度、Context 窗口、工作上下文三个层次。
3. **机制**：选择官方状态、结构化状态文件或安全适配器；不抓取凭证。
4. **路径**：先假数据样张，再接局域网数据；远程访问另行确认。
5. **表达**：应用 DeepWheel 横屏规范和手机安全区。
6. **交付**：生成 PWA、运行校验、给启动与恢复说明。

底层机制未锁定时，不进入远程控制、公开部署或完整会话展示。

## 第一步：能力体检

读取 `references/capability-preflight.md`，输出：

```text
当前可直接做：
当前需要工具或权限：
当前不承诺：
建议先做的最小测试：
是否需要安装或启用工具：是/否，安装前需确认
```

默认低消耗：先生成假数据静态样张，不读取历史会话，不扫描全盘，不安装第三方工具。

首次成功只要求完成一张能在浏览器打开的假数据横屏；后续再渐进披露真实状态、网络和通知。长状态源先抽样、后分段，不做无必要的全量解析。

面向新用户时，必须按 `生成演示 → 电脑校验 → 电脑预览 → 确认可信局域网 → 手机设备检查 → 添加到主屏幕 → 选择是否接真实数据` 的顺序引导，不得把安装、网络暴露和真实数据接入合并成一步。

PDF、扫描 PDF OCR、图片 OCR、视频和音频不属于本 Skill 的默认输入；若用户把这些内容当状态源，先说明需要额外工具与权限，并降级为用户提供结构化摘要。

## 第二步：建立状态合同

读取 `references/status-data-contract.md`。任何状态源都必须投影为最小、可清洗的统一字段。

必须分开：

- `quota`：额度、重置时间、成本；
- `sessions`：一个工具下的多个会话；
- `context_health`：只属于单个会话的上下文健康，多个会话不得相加；
- `work_context`：当前对象、目标、下一步、卡点和核实时间。

不得用 Token 百分比冒充工作进度，也不得从聊天全文推断用户的私人工作状态后直接展示。

默认提供三张手动切换视图，不自动轮播：

- `NOW`：每个工具最需要关注的两个会话和账号级用量；
- `SESSIONS`：每个工具最多四个会话摘要；
- `USAGE`：账号级额度、重置和核实来源。

## 第三步：选择实现层级

读取 `references/implementation-options.md`，默认按风险从低到高选择：

1. 静态假数据样张；
2. 本机结构化 JSON；
3. Claude/Codex 只读适配器或助手生成的清洗快照；
4. 私人网络访问；
5. 远程批准或控制。

第 4、5 层涉及安装、网络暴露或执行动作，必须先说明风险、降级方案和验收方式，并取得用户确认。

## 第四步：生成横屏 PWA

读取 `references/deepwheel-landscape-ui.md`；目标为 iPhone 或用户要求 Apple 平台适配时，同时读取 `references/apple-ios-alignment.md`。如用户要求生成文件，可使用：

```bash
python3 scripts/create_ai_monitor.py --output /path/to/new-output
```

脚本只允许写入不存在或为空的目标目录；不得覆盖现有文件。默认生成假数据，绝不复制本机状态、凭证或会话内容。

生成后运行：

```bash
python3 scripts/validate_ai_monitor.py /path/to/output
```

如果用户要在 iPhone 上完成首次成功，同时交付生成目录内的 `README.md`，并明确说明：`127.0.0.1` 只适用于电脑本机；使用 `0.0.0.0` 前要先确认可信 Wi-Fi；停止共享用 `Control+C`。

## 第五步：接数据

优先级：

1. 用户主动维护的 `CURRENT.md` / `HANDOFF.md` 等结构化入口；
2. 官方 CLI 或公开接口提供的状态；
3. 已审计的本机工具 JSON 输出；
4. 经过清洗的最小状态快照。

真实用量优先让用户从官方用量界面确认；没有稳定、公开、机器可读来源时使用手动值或 `null`，不要猜测。多会话只读取标题、状态、更新时间等最小元数据；不读取正文。

不得读取或回显 API Key、Token、Cookie、sessionKey、密码、私钥、验证码、完整敏感日志。不得把状态服务裸露到公网。

如果数据源只能通过浏览器 Cookie、非公开接口或完整 transcript 获得，明确标为高风险替代路径，不默认启用。

## 第六步：交付与验收

读取 `references/validation-checklist.md`。交付必须包括：

```text
完成了什么
手机如何打开
当前数据是模拟还是真实
隐私边界
卡点与降级方式
第一次成功的逐步引导
可信局域网的确认点与停止方式
下一步可选项
```

说完成前必须核验页面、文件和启动路径。相同原因失败最多重试两次，之后停下说明卡点。

## 独立产品入口

本 Skill 可独立接收文字目标、现有文件夹、状态 JSON 或网页目录，不要求用户预先安装 Claude HUD、CodexBar 或 Quality Gate。没有关联工具时，仍可完成假数据样张、状态合同、DeepWheel 横屏设计与静态校验。

## 能力边界

### 已支持

- 规划 Claude/Codex 双 Agent 横屏状态架构；
- 在两个 1:1 等宽 Provider 面板中管理多个会话；
- 提供 NOW / SESSIONS / USAGE 三视图；
- 生成无依赖、假数据优先的 PWA starter；
- 使用 DeepWheel 品牌 Logo 和 **AI Monitor** 应用短名；
- 默认跟随系统语言，并提供无 Cookie、无存储的 `EN／中` 切换；
- 区分额度、Context 窗口和工作上下文；
- 应用 DeepWheel 横屏视觉与安全区约束；
- 静态安全、结构和品牌约束校验；
- 给出局域网启动与添加到主屏幕说明。

### 需要工具、权限或人工复核

- 真实 Claude/Codex 用量与 Context 数据；
- 后台常驻服务；
- HTTPS、私人网络和远程访问；
- iPhone 真机横屏、安全区、200% 文本和长时间常亮测试；
- 第三方适配器的许可证与供应链审计。

### 暂不承诺

- 绕过平台登录或额度限制；
- 在所有 Claude/Codex 版本上稳定读取非公开状态；
- 自动安装、公开部署、push、Tag 或 Release；
- 安全地远程执行任意命令；
- 用 Token 数量准确判断任务是否完成。

## 关联 Skill 主动提醒

- 需要 Claude 终端内 HUD 时，可介绍 Claude HUD；不安装时使用模拟或结构化状态文件。
- 需要 Claude/Codex 用量聚合时，可介绍 CodexBar；不安装时仅显示手动或官方状态。
- 需要发布前审计时，建议调用 Lucas-DeepWheel Skill Quality Gate；未安装时按本 Skill 的检查清单降级。

任何关联工具都不得自动安装。

## 安全边界

- 不读取、保存、输出或扩散可复用凭证；
- 不显示完整聊天、完整终端日志、客户资料或私人文件正文；
- 不自动外发、删除、覆盖、安装、公开发布或改变网络可见性；
- 不把本机绝对路径、用户账号或内部项目名写进公开模板；
- 远程控制必须与只读状态屏分产品、分权限、分确认。

## 完成前验收

- 是否现场读取了用户提供的目标文件或目录；
- 是否先完成假数据最小成功，再接真实数据；
- 是否区分额度、Context 窗口和工作上下文；
- 是否把账号级用量与单会话 Context 严格分离；
- 是否标明已核实、推断和待确认；
- 是否运行生成物校验并查看横屏样张；
- 是否说明手机打开、失败恢复和不安装时的降级路径；
- 是否没有自动安装、外发、覆盖、公开发布或暴露网络；
- 是否没有读取、保存或输出敏感凭证和完整日志。
