import os
from flask import Flask, request

app = Flask(__name__)

# FIX 1: استفاده از Environment Variable به جای هاردکد کردن پسورد
# اگر پسورد ست نشده بود، یک مقدار پیش‌فرض امن‌تر یا خالی برمی‌دارد
DB_PASSWORD = os.environ.get("DB_PASSWORD")
AWS_KEY = os.environ.get("AWS_KEY")

@app.route('/')
def hello():
    return "<h1>Hello! This application is now SECURE :lock:</h1>"

@app.route('/hackme')
def hackme():
    # FIX 2: حذف کامل قابلیت اجرای دستورات سیستم عامل (Subprocess)
    # به جای اجرای دستور، فقط ورودی کاربر را نمایش می‌دهیم (بدون اجرا)
    target = request.args.get('target', 'unknown')
    
    # اینجا فقط یک پیام ساده برمی‌گردانیم. خطر Command Injection رفع شد.
    return f"Scanning target: {target} (Simulated - No real execution)"

if __name__ == '__main__':
    # FIX 3: غیرفعال کردن حالت دیباگ
    # پورت را هم می‌توانیم از متغیر محیطی بگیریم
    port = int(os.environ.get("PORT", 5000))
    
    # FIX 4: بایند کردن روی 0.0.0.0 در داکر اوکی است، اما debug باید False باشد
    app.run(host='0.0.0.0', port=port, debug=False)