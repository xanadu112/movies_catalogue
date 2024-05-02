from flask import Flask, render_template, url_for, request
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    available_lists = tmdb_client.get_available_lists()
    selected_list = request.args.get('list_type', 'popular')
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, available_lists=available_lists)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)

with app.test_request_context():
    print(url_for('movie_details', movie_id=""))



if __name__ == '__main__':
    app.run(debug=True)