import requests
from config import API_TOKEN






def get_movie_url_by_title(movie_title):
    api_key = API_TOKEN
    base_url = 'https://api.themoviedb.org/3/search/movie'

    params = {
        'api_key': api_key,
        'query': movie_title,
        'language': 'ru-RU'
}


    response = requests.get(base_url, params=params)
    data = response.json()


    if 'results' in data and data['results']:
        movie_id = data['results'][0]['id']
        movie_info = data['results'][0]
        movie_url = f'https://www.themoviedb.org/movie/{movie_id}'

        return f"{movie_url}\nName:   {movie_info['title']}\nYear:   {movie_info['release_date'][:4]}\nRating:   {movie_info['vote_average']}\nDescription:   {movie_info['overview']}\nTo exit click on /cancel"
    else:
        return f"You Entered The Name Incorrectly"

