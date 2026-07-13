# 第一次使用：10 分钟完成 iPhone 横屏副屏

目标：先用合成数据完成一次安全、可回退的横屏体验。此阶段不连接 Claude、Codex，不读取对话，也不安装后台服务。

## 开始前

你需要：

- 一台装有 Python 3.10 或更高版本的电脑；
- 一台 iPhone X 至 iPhone 17 Pro Max；
- 电脑与手机连接同一个你信任的 Wi-Fi；
- Safari。

你暂时不需要：API Key、Provider 登录、Node.js、第三方插件或公网服务器。

## 第 1 步：生成演示页

在仓库根目录运行：

```bash
python3 skills/lucas-deepwheel-ai-watchtower/scripts/create_watchtower.py \
  --output ./watchtower-demo
```

预期看到 `CREATED` 和 `MODE: demo data only`。如果目标目录非空，生成器会停止，不会覆盖原文件。

## 第 2 步：先在电脑上校验

```bash
python3 skills/lucas-deepwheel-ai-watchtower/scripts/validate_watchtower.py \
  ./watchtower-demo
```

预期结果：`CLEAN`。

## 第 3 步：先完成电脑端预览

```bash
cd watchtower-demo
python3 -m http.server 8765 --bind 127.0.0.1
```

电脑浏览器打开：

```text
http://127.0.0.1:8765
```

能看到 NOW / SESSIONS / USAGE 后，按 `Control+C` 停止服务，再进入手机步骤。

## 第 4 步：确认后开放到可信局域网

这一步会让同一局域网中的设备访问端口 `8765`。只在家庭或可信办公 Wi-Fi 中使用，不要在公共 Wi-Fi 或公网端口转发环境中使用。

确认后运行：

```bash
python3 -m http.server 8765 --bind 0.0.0.0
```

查找电脑的局域网 IP：

- macOS：`ipconfig getifaddr en0`；没有结果时尝试 `ipconfig getifaddr en1`；
- Windows：运行 `ipconfig`，查找当前网络的 IPv4 Address；
- Linux：运行 `hostname -I`。

假设电脑地址是 `192.168.1.20`，手机 Safari 打开：

```text
http://192.168.1.20:8765
```

不要在手机里填写 `127.0.0.1`，它只代表手机自己。

## 第 5 步：横屏诊断和全屏

1. 将 iPhone 旋转为横屏；
2. 打开 `http://电脑IP:8765/?debug=1`；
3. 确认诊断层显示 `PASS`、没有横向或纵向溢出；
4. Safari 点“分享”→“添加到主屏幕”；
5. 如系统提供选项，打开“作为 Web App 打开”；
6. 从主屏幕 AI Monitor 图标重新进入。
7. 默认跟随系统语言；如需切换，点右上角 `EN／中`。

黑色设备底、安全区和全屏视口规则覆盖 iPhone X 至 17 Pro Max 的横屏尺寸。自动化矩阵不能替代真机；刘海、灵动岛、显示缩放和系统文字大小仍应以你的设备结果为准。

## 第 6 步：选择下一层能力

第一次成功后，只选择一条继续：

1. **保持演示模式**：零数据接入，适合判断界面是否有价值；
2. **手动状态 JSON**：由你维护最小状态，不连接 Provider；
3. **只读真实数据适配器**：需要单独审计数据来源、权限、安装、后台运行和回退；
4. **私人网络访问**：属于更高风险步骤，必须再次确认，不默认开启。

不要从演示模式直接跳到抓取 Cookie、读取完整对话或公网暴露。

## 60 秒故障排查

| 现象 | 优先检查 |
|---|---|
| 手机打不开 | 两台设备是否同一 Wi-Fi；地址是否使用电脑局域网 IP；电脑防火墙是否允许 Python；是否被访客网络隔离 |
| 仍看到 Safari 工具栏 | 必须“添加到主屏幕”并从主屏幕图标进入 |
| 灵动岛或刘海挡住内容 | 确认横屏、刷新页面，并用 `?debug=1` 检查 safe area 与 overflow |
| 底部出现大块留白 | 确认使用当前 starter；当前版区分浏览器 `100dvh` 与主屏 `100lvh` |
| 电脑休眠后页面不更新 | 演示服务器依赖终端进程；唤醒电脑或重新运行命令 |
| 想停止共享 | 在运行服务器的终端按 `Control+C` |

## 第一次成功的验收标准

- [ ] 电脑端能打开演示页；
- [ ] 手机横屏能打开 NOW / SESSIONS / USAGE；
- [ ] `?debug=1` 显示 PASS；
- [ ] 主屏模式没有浏览器工具栏；
- [ ] 刘海／灵动岛不遮挡文字；
- [ ] 你知道当前使用的是合成数据；
- [ ] 你知道如何用 `Control+C` 停止服务。
