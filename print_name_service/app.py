from flask import Flask, render_template, request
from prometheus_client import Counter, Gauge, generate_latest, REGISTRY
from prometheus_client.exposition import MetricsHandler
import psutil

app = Flask(__name__)

request_counter = Counter('flask_requests_total', 'Total number of requests received')

cpu_usage = Gauge('flask_cpu_usage_percent', 'CPU usage percentage')

@app.route('/metrics')
def metrics():
    # Update CPU usage gauge
    cpu_percent = psutil.cpu_percent()
    cpu_usage.set(cpu_percent)

    # Generate metrics response
    return generate_latest(REGISTRY)

@app.route('/', methods=['GET', 'POST'])
def index():
    request_counter.inc()
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = None
    return render_template('name.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
