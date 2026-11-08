from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "iot-dashboard-demo-key")

# Demo sensor readings. Replace this function with real sensor/API integration.
def get_latest_data():
    return {
        "temperature": 25.0,
        "humidity": 60.0,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "运行正常",
    }

target_temperature = 26.0

@app.route("/")
def index():
    data = get_latest_data()
    return render_template("index.html", data=data, target_temperature=target_temperature)

@app.route("/set-temperature", methods=["POST"])
def set_temperature():
    global target_temperature
    raw_value = request.form.get("target_temperature", "").strip()
    try:
        value = float(raw_value)
        if not -20 <= value <= 60:
            raise ValueError
        target_temperature = value
        flash(f"目标温度已更新为 {value:.1f} ℃", "success")
    except (TypeError, ValueError):
        flash("请输入 -20 ℃ 至 60 ℃ 之间的有效温度。", "error")
    return redirect(url_for("index"))

@app.route("/api/status")
def api_status():
    data = get_latest_data()
    data["target_temperature"] = target_temperature
    return data

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
