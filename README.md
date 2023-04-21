# Basic Blog Application with Flask
This repository contains examples of a basic blog application implemented using Flask.

The Flask application displays a list of blog posts on the homepage and allows users to view individual blog posts by clicking on their titles.

The application uses a Post class (in post.py) to represent each blog post. The main.py script retrieves example posts in JSON format from an API, creates Post objects, and stores them in a list. The Flask application then uses this list to render the appropriate blog posts on different pages.

The templates folder contains the HTML templates used by the Flask application for rendering the homepage (index.html) and individual blog post pages (post.html).

The static/css folder contains the styles.css file, which provides styling for the HTML templates.

To run the Flask application, simply execute the main.py script.