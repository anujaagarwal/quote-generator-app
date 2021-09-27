Quote Generator App with Flask and Vue.js
=====

About the project
----
This application mainly fetches quotes from [this site](http://www.quotationspage.com/random.php) using Flask Api and then displays it in Vue app beautifully with the following features. 

- Copy to clipboard feature
- Download button to get quote.png file of that quote
- loader, scollbar, gifs and button effects

Client folder in the project has all the frontend coding and backend coding is in server folder.

Overall Challenge faced
--

- Learning a new framework(vue.js) and implementing it end to end


Specific challenges
--

- wrapping my quotes in a canvas
- Still facing issues while deployement and hosting

Futute feature enhancements
-----

- Add social media buttons to directly share the quote over net
- Read more feature in a long quote, but I fear it may degrade the user experience as the main purpose is to show quotes clearly.


Learnings
----

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

