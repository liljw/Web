# tmdb
# the movie database

import requests

API_KEY = '29df6583a904bc9dd4937f055eb9d731'

URL = 'https://api.themoviedb.org/3/movie/popular?'
URL += f'api_key={API_KEY}&language=ko-kr'

res = requests.get(URL).json()

popular_movies = res['results']

# 평점순으로 정렬하기
# 성인영화만 필터링하기
# 2023년 영화만 필터하기