from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')  # Make sure this exists!
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    # Get current server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get `top` command output
    top_output = subprocess.run(["top", "-bn", "1"], capture_output=True, text=True).stdout

    # Prepare response
    response = f"""
    <pre>
    Name: Yojitha Bondalapati
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
