from flask import Flask
import business 
from flask import jsonify

app = Flask(__name__)

port= 3000

@app.route("/", methods=['GET'])
def list_movies_sort():
    sorted_list= business.get_movies_sorted()
    return jsonify(sorted_list)

@app.route("/characters", methods=['GET'])
def list_characters():
    characters_list= business.get_characters("1")
    return jsonify(characters_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)