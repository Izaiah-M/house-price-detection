from flask import Flask, request, jsonify
import service

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

# Need a route to return our locations from bangaluru
@app.route("/locations")
def get_locations():
    response = jsonify({
        "locations": service.get_locations()
    })

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == "__main__":
    print("starting home price prediction flask server...")
    app.run()