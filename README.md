Quote Generator App with Flask and Vue.js
=====

This application mainly fetces quotes from [this site](http://www.quotationspage.com/random.php) and then displays it in vue app beautifully with the following features

- Copy to clipboard feature
- Download button to get quote.png file of that quote
- loader, scollbar and button effects

Overall Challenge faced

- Learning a new framework(vue.js) and implementing it end to end
- Still facing issues while deployement and hosting

Specific challenges

- wrapping my quotes in a canvas
- work on button effects

Futute feature enhancements

- Add social media buttons to directly share the quote over net.



Learnings

- How vue.js works
- canvas tag
- How flask and vue can be connected

Want to use this project?
-----

Step 1:Fork/Clone

Run the server-side Flask app in one terminal window:

> $ cd server

> $ python3.9 -m venv env

> $ source env/bin/activate

> (env)$ pip install -r requirements.txt

> (env)$ python app.py

Navigate to [I fetch 10 quotes from the quotes site](http://localhost:5000/quote/random)


Run the client-side Vue app in a different terminal window:

> $ cd client

> $ npm install

> $ npm run serve

Navigate to [Yeah! you can see my web app](http://localhost:8080)

Here is what it looks like!
-----
![](project.gif)

