import requests


def get_popular_movies(page=1):
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }

    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data["results"]
    else:
        print(f"Error get popular movies: {response.status_code}")
        return []

def get_toprated_movies(page=1):
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data["results"]
    else:
        print(f"Error get top rated movies: {response.status_code}")
        return []

def get_movies_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print(f"Error get top rated movies: {response.status_code}")
        return{}     



def get_movies_images(movie_id):
    url= f"https://api.themoviedb.org/3/movie/{movie_id}/images" 
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print(f"Error get top rated movies: {response.status_code}")
        return{}  

def get_movies_recommendations(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data["results"]
    else:
        print(f"Error get top rated movies: {response.status_code}")
        return[] 

def get_movies_videos(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US" 
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data["results"]
    else:
        print(f"Error get top rated movies: {response.status_code}")
        return[]        
def search_movies(query:str, page: int):
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }

    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data["results"]
    else:
        print(f"Error search movies: {response.status_code}")
        return []    