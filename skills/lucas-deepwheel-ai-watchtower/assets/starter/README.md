# DeepWheel AI Monitor starter｜首次使用

This folder contains synthetic demo data only. It does not read Claude, Codex, credentials, transcripts, browser storage, or project files.

本目录只包含合成演示数据，不读取 Claude、Codex、凭证、对话、浏览器存储或项目文件。

## 1. Preview on this computer｜先在电脑预览

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765`. Confirm NOW, SESSIONS, and USAGE render, then press `Control+C`.

打开 `http://127.0.0.1:8765`。确认三个页面可见后，按 `Control+C` 停止。

## 2. Use an iPhone on trusted Wi-Fi｜可信 Wi-Fi 手机访问

This exposes port `8765` only to the local network. Confirm that the Wi-Fi is trusted and that no public port forwarding is enabled.

此步骤会把端口 `8765`开放给同一局域网。请先确认使用家庭或可信办公 Wi-Fi，且没有公网端口转发。

```bash
python3 -m http.server 8765 --bind 0.0.0.0
```

Find the computer LAN IP:

- macOS: `ipconfig getifaddr en0` (try `en1` if empty)
- Windows: `ipconfig`
- Linux: `hostname -I`

If the address is `192.168.1.20`, open this on the iPhone:

```text
http://192.168.1.20:8765/?debug=1
```

Do not use `127.0.0.1` on the phone; it points back to the phone itself.

手机不能使用 `127.0.0.1`，必须填写电脑的局域网 IP。

## 3. Full screen｜全屏模式

Rotate to landscape. In Safari choose Share → Add to Home Screen, enable Open as Web App when available, then launch from the AI Monitor Home Screen icon.

将手机旋转为横屏，在 Safari 选择“分享”→“添加到主屏幕”，如有选项则启用“作为 Web App 打开”，之后从主屏幕图标进入。

The current starter adapts from iPhone X through 17 Pro Max, uses safe-area guards for notches and Dynamic Island, and separates browser `100dvh` from Home Screen `100lvh` to avoid bottom blank space.

当前 starter 覆盖 iPhone X 至 17 Pro Max 横屏尺寸，并针对刘海、灵动岛和主屏模式底部留白做安全区与视口适配。

AI Monitor follows the system language by default. Use the compact `EN／中` control in the top-right corner to switch without storing a language preference.

AI Monitor 默认跟随系统语言。右上角 `EN／中` 可随时切换，不会保存语言偏好。

## 4. Stop and recover｜停止与排查

- Stop sharing: press `Control+C` in the server terminal.
- Phone cannot open: check same Wi-Fi, computer LAN IP, firewall, and guest-network isolation.
- Safari bars remain: launch from the Home Screen icon.
- Overlap or blank space: reload the current starter with `?debug=1` and confirm PASS.

- 停止共享：在服务器终端按 `Control+C`。
- 手机打不开：检查同一 Wi-Fi、电脑 IP、防火墙和访客网络隔离。
- 仍有浏览器栏：必须从主屏幕图标进入。
- 遮挡或留白：使用当前版本并通过 `?debug=1` 检查 PASS。

Do not expose this server to the public internet. Real data, background services, HTTPS, and private networking require a separate review and explicit approval.

不要把服务暴露到公网。真实数据、后台常驻、HTTPS 和私人网络必须单独审计并明确授权。
