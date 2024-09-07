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

# Route to predict the home Price 
@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        "estimated_home_price": service.get_estimated_price(location,sqft=total_sqft, bhk=bhk, bath=bath)
    })

    return response
    

if __name__ == "__main__":
    print("starting home price prediction flask server...")
    app.run()