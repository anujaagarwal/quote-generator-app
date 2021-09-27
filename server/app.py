# import dependencies
from flask import Flask, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

# instantiate the app and point to vue
app = Flask(__name__,static_folder='../client/dist/',static_url_path='/')
app.config["DEBUG"] = False

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Making GET request
@app.route('/quotes/random', methods=['GET'])
def getRandomQuotes():
    offset = int(request.args.get('offset'))
    if offset < 1 or offset > 100:
        return { 'error' : 'Illegal offset!' , 'success' : False }
    # URL given in the task to get random quotes
    URL = "http://www.quotationspage.com/random.php" 
    req = requests.get(URL)
    list = []
    key = 0
    soup = BeautifulSoup(req.text, 'html.parser')
    # storing all the <a> tags inside quotes
    quotes = soup.find_all('dt', {'class' : 'quote'})
    for quote in quotes:
        if len(list) < offset:
            dict = {}
            dict['id'] = key
            dict['message'] = quote.a.text
            list.append(dict)
            key = key+1
    # can't directly return list in flask
    print(list)
    return { 'items': list, 'success' : True }
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
