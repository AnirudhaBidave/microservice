from flask import Flask, jsonify, redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# Example route to redirect to the To-Do List microservice
@app.route('/todos')
def redirect_to_todo_list():
    # Assuming your To-Do List microservice is running on port 5001
    return redirect("http://192.168.59.100:30003", code=302)

# Example route to redirect to the Calculator microservice
@app.route('/calculator')
def redirect_to_calculator():
    # Assuming your Calculator microservice is running on port 5002
    return redirect("http://192.168.59.100:30001", code=302)

# Example route to redirect to the Print Name microservice
@app.route('/print-name')
def redirect_to_print_name():
    # Assuming your Print Name microservice is running on port 5003
    return redirect("http://192.168.59.100:30002", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
