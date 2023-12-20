from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Adjust the origin as needed

SPOONACULAR_API_KEY = '375707f9a9a64601add1fdda656a97c0'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/recipes')
def get_recipes():
    query = request.args.get('query')
    app.logger.info(f"Received request for recipes with query: {query}")

    recipes = fetch_recipes_from_api(query)
    app.logger.info(f"Returning recipes: {recipes}")

    return jsonify(recipes)

def fetch_recipes_from_api(query):
    endpoint = 'https://api.spoonacular.com/recipes/search'
    params = {
        'query': query,
        'apiKey': SPOONACULAR_API_KEY,
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    recipes = [{'id': recipe['id'], 'title': recipe['title']} for recipe in data.get('results', [])]
    return recipes

if __name__ == '__main__':
    app.run(debug=True)