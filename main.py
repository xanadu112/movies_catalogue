from flask import Flask, render_template, url_for, request
import tmdb_client

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    list_types = [
        'top_rated',
        'upcoming',
        'popular',
        'now_playing'
    ]
    if selected_list not in list_types:
        selected_list = 'popular' 
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    movie_info = [tmdb_client.get_movie_info(movie) for movie in movies]
    return render_template("homepage.html", movies=movies, movie_info=movie_info, list_types=list_types, current_list=selected_list)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)

with app.test_request_context():
    print(url_for('movie_details', movie_id=""))


if __name__ == '__main__':
    app.run(debug=True)