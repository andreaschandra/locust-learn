from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return jsonify({"message": "This is homepage"})

@app.route("/createuser", methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return jsonify({"message": "createuser GET"})
    else:
        return jsonify({
            "message": "OK",
            "fullname": request.form['fullname'],
            "gender": request.form['gender']
        })

@app.route("/createuserjson", methods=['GET', 'POST'])
def create_user_json():
    if request.method == 'GET':
        return jsonify({"message": "createuser GET"})
    else:
        content = request.json
        return jsonify({
            "message": "OK",
            "fullname": content['fullname'],
            "gender": content['gender']
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0")
