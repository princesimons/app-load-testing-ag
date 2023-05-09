from flask import Flask, render_template, request
import requests
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        num_requests = int(request.form['num_requests'])
        timeout = float(request.form['timeout'])

        response_times = []
        bytes_sent_list = []
        for i in range(num_requests):
            try:
                start_time = time.time()
                response = requests.get(url, timeout=timeout)
