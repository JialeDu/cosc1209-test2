from flask import Flask
import socket

app = Flask(__name__)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

@app.route("/")
def home():
    return f"Hello Cloud from ECS! Dujiale Host: {hostname}, IP: {ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
