# importar flask
from flask import Flask, jsonify, request
import requests
# incializar flaks 
app = Flask(__name__)

@app.route('/get_pokemon_data', methods=['GET'])
def get_pokemon_data():
    # URL de la API de Pokémon para el Pokémon "Ditto"
    api_url = 'https://pokeapi.co/api/v2/pokemon/ditto'

    # Realizar la solicitud GET a la API
    response = requests.get(api_url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON y devolverla
        pokemon_data = response.json()
        return jsonify(pokemon_data)
    else:
        # Si la solicitud no fue exitosa, devolver un mensaje de error
        return jsonify({'error': 'No se pudo obtener los datos del Pokémon'}), 500


# definir ruta
@app.route('/api', methods=['GET'])
def get_api():
    return jsonify({'mensaje':'hola mundo'})

#ejecutar el servidor flask 
if __name__ == '__main__':
    app.run(debug=True, port=4000)
    