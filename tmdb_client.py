import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NDNkNGI0NmQzYmJjNjBlYzVmYzM0YTVkNGMyMjg1OSIsInN1YiI6IjY2MmMwYjRhNjJlODZmMDEyYzkxMDhlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BDUdzy2HFr66ENL0rrJALRS_gPrIxBC5Azc9Tb4bLmA"

def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_movie_info(movie):
    movie_id = movie['id']
    title = movie['title']
    return {"id": movie_id, "title": title}

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]