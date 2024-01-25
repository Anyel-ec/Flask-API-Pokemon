# importar las librerias de Flask
from flask import Flask, render_template, request, jsonify
import requests

# instanciar la clase Flask
app = Flask(__name__)

# definir la ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    # si el metodo es POST
    if request.method == 'POST':
        # obtener el nombre del pokemon
        pokemon_name = request.form.get('nombre')
        pokemon_data = get_pokemon_data(pokemon_name)
        # enviar los datos al index.html 
        return render_template('index.html', pokemon_data=pokemon_data)
    # si el metodo es GET
    return render_template('index.html', pokemon_data=None)



# definir la ruta para obtener los datos del pokemon
def get_pokemon_data(pokemon_name):
    # si el nombre del pokemon existe
    if pokemon_name:
        # obtener los datos del pokemon
        api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
        # hacer la peticion a la API
        response = requests.get(api_url)

        # si la peticion fue exitosa
        if response.status_code == 200:
            # retornar los datos del pokemon
            return response.json()
    # si la peticion no fue exitosa
    return None

# Nueva ruta para obtener sugerencias de nombres de Pokémon
@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    search_value = request.form.get('search_value')

    # Obtener sugerencias de nombres de Pokémon que coincidan con la entrada
    suggestions = [pokemon['name'] for pokemon in get_pokemon_list() if pokemon['name'].startswith(search_value.lower())]

    # Renderizar las sugerencias como una lista HTML
    suggestions_html = ''.join(f'<a href="#" class="list-group-item list-group-item-action">{suggestion}</a>' for suggestion in suggestions)

    return suggestions_html


# definir la ruta para obtener la lista de pokemones
def get_pokemon_list():
    # obtener la lista de pokemones
    api_url = 'https://pokeapi.co/api/v2/pokemon/'
    # hacer la peticion a la API
    response = requests.get(api_url)
    # si la peticion fue exitosa
    if response.status_code == 200:
        # retornar la lista de pokemones
        return response.json()['results']
    # si la peticion no fue exitosa
    return []


# definir la ruta para obtener los datos del pokemon
if __name__ == '__main__':
    app.run(debug=True)
