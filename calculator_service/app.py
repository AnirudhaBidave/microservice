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
def calculator():
    request_counter.inc()
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        operator = request.form['operator']
        num2 = float(request.form['num2'])

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            result = None

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
