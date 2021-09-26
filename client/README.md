Developing a Single Page App with Flask and Vue.js

Want to use this project?
Step 1:Fork/Clone

Run the server-side Flask app in one terminal window:

$ cd server
$ python3.9 -m venv env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
(env)$ python app.py
Navigate to http://localhost:5000/quote/random

Run the client-side Vue app in a different terminal window:

$ cd client
$ npm install
$ npm run serve
Navigate to http://localhost:8080

