from flask import Flask, render_template

app = Flask(__name__)

# List of movies
movies = [
    {"title": "The Shawshank Redemption", "year": 1994, "genre": "Drama", "poster": "static/images/w.jpg"},
    {"title": "The Godfather", "year": 1972, "genre": "Crime, Drama", "poster": "static/images/q.jpg"},
    {"title": "The Dark Knight", "year": 2008, "genre": "Action, Crime, Drama", "poster": "static/images/es.jpg"},
    {"title": "Pulp Fiction", "year": 1994, "genre": "Crime, Drama", "poster": "static/images/pp.jpg"}
]

# Route to display movies   
@app.route('/')
def index():
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
