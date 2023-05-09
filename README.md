# app-load-testing-ag
App Load Testing AG is a Python-based application that allows you to hit a supplied HTTP endpoint and a variable number of times while returning information and statistics about response times, bytes sent, and more. The application can be run either as a command-line tool or as a web application
# Requirements
1. Python 3.7 or later
2. Flask
3. Requests

# Installation
1. Clone the Github repository:
```console
git clone https://github.com/princesimons/app-load-testing-ag.git
```
2. Change directory to the cloned repository:

```console
cd app-load-testing-ag
```
3. Install the dependencies:

```console
pip install Flask requests
```
# Usage
To use the command-line tool, run the following command:
```css
python load_tester.py --url <endpoint-url> --num_requests <num-requests> --timeout <timeout-value>
```
Replace <endpoint-url> with the URL of the endpoint you want to hit, <num-requests> with the number of times you want to hit the endpoint (default is 10), and <timeout-value> with the timeout value for each request (default is 1 second).
  
# Web Application
To use the web application, run the following command: 
```console
python app.py
```
Then, open your web browser and navigate to http://localhost:5000.

Enter the URL of the endpoint you want to hit, the number of times you want to hit the endpoint, and the timeout value. Click the "Submit" button.

The web app will display the results in a graphical manner.
  
#Contributing
Contributions to App Load Testing AG are welcome. If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.
  
#License
  
App Load Testing AG is licensed under the MIT License. See the LICENSE file for more information.
