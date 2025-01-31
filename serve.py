from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Start stress_cpu.py in a non-blocking manner
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return f"push EC2 instance {socket.gethostbyname(hostname)} to maximum CPU utilization"

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
