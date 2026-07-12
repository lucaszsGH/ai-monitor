# Apple iOS 对齐说明

## 使用目的

借鉴 Apple Human Interface Guidelines 的平台原则，不复制 Apple App 资产或逐像素仿制系统界面。DeepWheel 保持自己的品牌、色彩和组件语言。

## 本项目采用的原则

### 1. Hierarchy / Harmony / Consistency

- Claude 与 Codex 是同层级 Agent，使用等宽、同构、同基线卡片。
- 控件层级高于信息层级，但不以厚重装饰压过内容。
- 圆角、圆形进度与设备曲线保持同心感；两卡结构和指标位置一致。

依据：[Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)。

### 2. Safe areas

- 背景可延伸到物理屏幕边缘；文字、指标和按钮必须进入安全区。
- 使用 `viewport-fit=cover` 和 `env(safe-area-inset-*)`，并在 iPhone X 至 17 Pro Max 级尺寸做保守 inset 模拟。

依据：[Apple HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) 与 [WebKit iPhone X safe-area guidance](https://webkit.org/blog/7929/designing-websites-for-iphone-x/)。

### 3. Typography and Dynamic Type

- UI 文本优先 Apple 系统字体栈，品牌锁定区继续使用 DeepWheel 品牌字体栈。
- 保持短标签和清晰层级；支持至少模拟 200% 文本缩放，真机仍需 Dynamic Type 验收。
- 重要图标随文本级别保持可读，不用极细字重。

依据：[Apple HIG Typography](https://developer.apple.com/design/human-interface-guidelines/typography) 与 [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility/)。

### 4. Color and status

- 颜色只承担品牌焦点、状态和反馈；相同颜色不表达相反含义。
- 状态同时用文字、图标和颜色：工作中=绿色+勾+文字；等待=橙色+时钟+文字。状态色只用于 Agent 状态轨和胶囊，不污染 Context 健康含义。
- 品牌蓝只保留 logo 点和唯一主行动，不把所有进度条染蓝。

依据：[Apple HIG Color](https://developer.apple.com/design/human-interface-guidelines/color)；不得只靠颜色区分信息。

### 5. Progress and chart semantics

- Context 是“已使用容量”，采用顺时针圆环并明确写“已用”；圆环颜色按使用健康阈值表达，不跟随 Agent 的工作/等待状态。
- Quota 是“剩余额度”，采用从左到右的线性条并明确写“剩余”。
- 百分比必须来自可说明的来源；未知时显示不可用，不伪造精度。
- 圆环和线性条保持固定位置，不在同一指标生命周期里切换形态。

依据：[Apple HIG Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) 与 [Charts](https://developer.apple.com/design/human-interface-guidelines/charts)。HIG 的 Fitness/Stocks 案例说明关键数据要有上下文、颜色之外还要有形状和文字。

### 6. Interaction

- 主按钮命中区不小于 44×44pt。
- 首屏只保留一个主行动；状态卡本身默认只读。
- 数据过期、断网和服务停止必须提供恢复提示，不能只显示静止进度。

## 不采用

- 不直接复制 Liquid Glass、系统图标资产或 Apple Design Resources。
- 不用玻璃拟态掩盖 DeepWheel 信息层级。
- 不把 Context 或 Quota 伪装成任务完成进度。
- 不因模仿 Apple 而牺牲 DeepWheel 的墨、白、雾灰和克制蓝预算。
