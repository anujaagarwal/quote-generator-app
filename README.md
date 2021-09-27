Quote Generator App with Flask and Vue.js
=====

  # Table of Contents

  * [About the project](#About the project)
  * [About the project structure](#About the project structure)
  * [Overall Challenge faced](#Overall Challenge faced)
  * [Specific challenges](#Specific challenges)
  * [Futute feature enhancements](#Futute feature enhancements)
  * [Learnings](#Learnings)
  * [Experience](#Experience)
  * [STEPS TO GET STARTED](#STEPS TO GET STARTED)
  * [Here is what it looks like!](#Here is what it looks like!)


  ## About the project

  This application mainly fetches random quotes(offset can be set by you) from [this site](http://www.quotationspage.com/random.php) using Flask Api and then displays it in Vue app beautifully with the following features. 

  - Copy to clipboard feature
  - Download button to get quote.png file of that quote
  - loader, scollbar, gifs and button effects

  ## About the project structure

  - Client folder in the project has all the frontend coding and backend coding is in server folder.

  # Overall Challenge faced

  - Learning a new framework(vue.js) and implementing it end to end

  ## Specific challenges

  - wrapping my quotes in a canvas
  - Still facing issues while deployement and hosting

  ## Futute feature enhancements

  - Add social media buttons to directly share the quote over net
  - Read more feature in a long quote, but I fear it may degrade the user experience as the main purpose is to show quotes clearly.

  ## Learnings

  - How vue.js works
  - canvas tag
  - How flask and vue can be connected

  ## Experience

  - Started loving Vue.js
  - So, fast to learn and lightweight
  - Really enjoyed the challenges faced and learning part

  Friend: Your project looks cool!
  ---
  Me: Want to use this project and contribute in it?
  ---
  Friend: Yes!
  ---
  Me: Follow the steps below
  ---

  ## STEPS TO GET STARTED

  Step 1:Fork/Clone

  ## Backend

  ### Prerequisities
  - pip
  - virtualenv
  - python v > 3.0

  ### Running the Flask App
  Run the server-side Flask app in one terminal window:

  ```sh
  $ cd server
  ```
  ```sh
  $ python3.9 -m venv env
  ```
  ```sh
  $ source env/bin/activate
  ```
  ```
  (env)$ pip install -r requirements.txt
  ```
  ```sh
  (env)$ python app.py
  ```
  Navigate to [This fetch quotes from the quotes site](http://localhost:5000/quote/random)

  ## Frontend

  ### Prerequisities

  - Node >= v8.0.0
  - npm >= 6.14.8

  ### Running the Vue App
  Run the client-side Vue app in a different terminal window:
  ```sh
  $ cd client
  ```
  ```sh
  $ npm install
  ```
  ```sh
  $ npm run serve
  ```

  Navigate to [Yeah! you can see my web app](http://localhost:8080)

  ## Here is what it looks like!
  ![](project.gif)

