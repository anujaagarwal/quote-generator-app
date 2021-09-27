from flask_frozen import Freezer
from server import getRandomQuotes

# Calls the application factory function to construct a Flask application
app = getRandomQuotes()

# Create an instance of Freezer for generating the static files from
# the Flask application routes
freezer = Freezer(app)


if __name__ == '__main__':
    # Run the development server that generates the static files
    # using Frozen-Flask
    freezer.run(debug=True)
