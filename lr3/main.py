from flask import Flask
import json
from utils import factorial1, factorial2

app = Flask(__name__)
CACHE_LOADED = False

def save_to_file(filename, cache):
    with open(filename, "w") as file:
        json.dump(cache, file)

def load_from_file(filename):
    with open(filename, "r") as file:
        return json.load(file)

@app.route("/")
def home():
    return "<p>Hello, world!</p>"

@app.route("/about")
def about_author():
    return "<p>Рамаз Сафин</p>"

@app.route("/calculate/<string:func>/<int:number>")
def calculate_factorial(func, number):
    global CACHE_LOADED
    if func == 'f1':
        result = str(factorial1(number))
        return f'Факториал числа {number} равен {result}'
    elif func == 'f2':
        result = str(factorial2(number))
        return f'Факториал числа {number} равен {result}'

@app.route("/load_cache")
def load_cache():
    global CACHE_LOADED
    CACHE_LOADED = True
    cache_data = load_from_file('cache.json')
    factorial1.cache = cache_data
    factorial2.cache = cache_data
    return f'Кэш загружен: {cache_data}'

@app.route("/save_cache")
def save_cache():
    global CACHE_LOADED
    if not CACHE_LOADED:
        load_cache()
    cache_data = {**factorial1.cache, **factorial2.cache}
    save_to_file('cache.json', cache_data)
    return f'Кэш сохранен: {cache_data}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
