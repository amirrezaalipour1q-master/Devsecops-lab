from flask import Flask, request
import subprocess

app = Flask(__name__)

# گاف امنیتی ۱: هاردکد کردن رمزها (خوراک اسکنرها!)
DB_PASSWORD = "super_secret_password_123"
AWS_KEY = "AKIA_FAKE_KEY_12345"

@app.route('/')
def home():
    return "<h1>Day 1: The Vulnerable App is Live!</h1>"

@app.route('/hackme')
def hackme():
    # گاف امنیتی ۲: گرفتن ورودی کاربر بدون چک کردن
    target = request.args.get('target')
    
    # گاف امنیتی ۳: Command Injection (خطرناک‌ترین باگ ممکن)
    # اینجا هر چی کاربر بفرسته مستقیم میره تو ترمینال لینوکس اجرا میشه!
    command = f"ping -c 1 {target}"
    
    try:
        # اجرای دستور در سیستم عامل
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return f"<pre>{output.decode('utf-8')}</pre>"
    except Exception as e:
        return f"<pre>Error: {str(e)}</pre>"

if __name__ == '__main__':
    # اجرا روی پورت ۵۰۰۰ و با دسترسی عمومی
    app.run(host='0.0.0.0', port=5000, debug=True)