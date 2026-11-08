# IoT 环境监控控制台

基于 Flask 的物联网网页 Demo，提供环境温度、湿度展示和目标温度设置功能。

## 功能
- 展示模拟传感器采集的当前温度（25.0 ℃）和湿度（60.0%）
- 展示当前目标温度
- 通过表单提交新的目标温度，后端校验并更新
- 提供 `/api/status` JSON 状态接口
- 响应式页面，支持桌面端和移动端

> 当前传感器数据为模拟数据。接入真实硬件时，可替换 `app.py` 中的 `get_latest_data()`。

## 本地运行
建议使用 Python 3.9 或更高版本。

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

浏览器访问 http://127.0.0.1:5000

## Render 部署
1. 将项目推送到自己的 GitHub 仓库。
2. 在 Render 中创建 **Web Service** 并连接该仓库。
3. Build Command：`pip install -r requirements.txt`
4. Start Command：`gunicorn app:app`
5. 点击 Deploy，完成后使用 Render 提供的网址访问。

## 项目结构
```text
IoT_Dashboard/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```
