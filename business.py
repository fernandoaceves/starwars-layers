import os
from flask import Flask
import requests

print("Application startup")
#port = int(os.environ['PORT'])
#print("PORT::", port)
port = 3000

app = Flask(__name__)

movie_url = "https://swapi.dev/api/films"

def get_movies_sorted():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]}
              for movie in data["results"]]
    sorted_movies = sorted(movies, key=lambda x: x["id"])
    return sorted_movies


def get_characters(id_movie):
    movie_url_esp = "https://swapi.dev/api/films/"
    movie_url_id= movie_url_esp + id_movie
    ls_char = []
    data = requests.get(movie_url_id).json()
    for url_character in data["characters"]:
        data_ch = requests.get(url_character).json()
        char_ls = {"name": data_ch["name"]}
        ls_char.append(char_ls)
    return ls_char