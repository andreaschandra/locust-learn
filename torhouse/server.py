import logging
from flask import Flask, request, jsonify, render_template
from model import sentclf

app = Flask(__name__)
logging.basicConfig(filename='error.log',level=logging.DEBUG)


@app.route("/")
def homepage():
    return jsonify({"message": "This is homepage"})


@app.route("/createuser", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        return jsonify({"message": "createuser GET"})
    else:
        return jsonify(
            {
                "message": "OK",
                "fullname": request.form["fullname"],
                "gender": request.form["gender"],
            }
        )


@app.route("/createuserjson", methods=["GET", "POST"])
def create_user_json():
    if request.method == "GET":
        return jsonify({"message": "createuser GET"})
    else:
        content = request.json
        return jsonify(
            {
                "message": "OK",
                "fullname": content["fullname"],
                "gender": content["gender"],
            }
        )


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return jsonify({"message": "Please use POST method to predict sentiment from a review"})
    else:
        content = request.json
        logging.debug("REVIEW: " + content["review"])
        label = sentclf(content["review"])
        return jsonify(
            {
                "label": label
            }
        )


if __name__ == "__main__":
    
    app.run(host="0.0.0.0")
