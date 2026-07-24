# AI Monitor v1.0.0｜把 iPhone 变成 Claude + Codex 状态副屏

把闲置或充电中的 iPhone 横放在 Mac 旁。Claude 或 Codex 是否正在等你、订阅额度还剩多少、最近主要用了什么模型，抬眼就能看到，不用反复切换窗口。

支持 Claude 单开、Codex 单开和双开。状态在 Mac 本机处理，不读取对话正文。

![AI Monitor 双工具 NOW 页面](https://raw.githubusercontent.com/lucaszsGH/ai-monitor/main/assets/showcase/01-dual-now-zh.png)

## 你会得到

- **不漏处理：** 等待、执行和待验收状态持续可见；
- **提前看额度：** Claude 与 Codex 各自显示剩余额度和重置时间；
- **看清消耗去向：** 从高消耗会话到模型用量结构；
- **按习惯使用：** 中文／English，Claude 单开、Codex 单开或双开；
- **不读取正文：** 状态只在 Mac 本机处理。

![AI Monitor Claude 与 Codex 单工具自适应界面](https://raw.githubusercontent.com/lucaszsGH/ai-monitor/main/assets/showcase/02-single-adaptive-zh.png)

## 下载

适用于 Apple 芯片 Mac（M1 或更新）、macOS 14 或更新版本，以及 iPhone X 至 iPhone 17 Pro Max 横屏。

**安装包：** `AI-Monitor-1.0.0-build.21-macOS-arm64-unsigned.dmg`

**SHA-256：** `cd39ff4acd8477f55ba4612f36df33f5ff3e353f0e9220f11b7a8562dc35bff8`

## 三步开始

1. 打开 DMG 内的 **1 · 安装指南 · GUIDE**，再安装 AI Monitor；
2. 让 iPhone 与 Mac 连接同一可信 Wi‑Fi，打开局域网私密链接；
3. Safari 点“分享 → 添加到主屏幕”，横屏放在 Mac 旁。

当前 App 尚未经过 Apple 公证。首次打开可能需要在“系统设置 → 隐私与安全性”中选择一次“仍要打开”。不需要关闭 Mac 安全保护，也不需要执行终端命令。

![AI Monitor 从 Mac 安装到添加为 iPhone 主屏副屏的三步流程](https://raw.githubusercontent.com/lucaszsGH/ai-monitor/main/assets/showcase/06-install-zh.png)

## 隐私与许可

只有同一局域网内持有完整私密链接的设备才能访问状态摘要。分享链接即允许对方查看摘要，请只在确实希望他人查看时分享。

本仓库公开材料按 MIT License 提供；DMG 内的 App 二进制包含私有本机运行核心，适用安装包内单独的二进制许可。Claude、Anthropic、OpenAI、GPT 与 Codex 等名称和标识仅用于识别对应工具，不表示赞助、背书或合作。

如果 AI Monitor 在你的 Mac 旁找到了固定位置，欢迎给项目一个 Star，也欢迎通过 Issue 与 PR 一起完善公开文档、适配和使用体验。

---

# AI Monitor v1.0.0｜Turn your iPhone into a Claude + Codex status screen

Place a spare or charging iPhone beside your Mac. See when Claude or Codex needs you, how much subscription capacity remains, and which models you have been using—without reopening every AI window.

Run Claude, Codex, or both. Status is processed locally on your Mac, and chat content is never read.

## Download

Requires an Apple Silicon Mac (M1 or later) running macOS 14 or later. The landscape dashboard supports iPhone X through iPhone 17 Pro Max.

**File:** `AI-Monitor-1.0.0-build.21-macOS-arm64-unsigned.dmg`

**SHA-256:** `cd39ff4acd8477f55ba4612f36df33f5ff3e353f0e9220f11b7a8562dc35bff8`

The build is not Apple-notarized. Open **1 · 安装指南 · GUIDE** inside the DMG and follow the visual one-time approval steps. Do not disable macOS security and do not run Terminal commands.

Only devices on the same network that possess the complete private link can access the status summary. Sharing the link grants access to that summary.

Public repository materials use the MIT License unless stated otherwise. The downloadable App contains a private local runtime and uses the separate binary license bundled with the App.
