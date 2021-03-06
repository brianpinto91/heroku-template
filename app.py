import flask

app = flask.Flask(__name__, template_folder="./templates")

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return flask.render_template("home.html")

@app.route("/about", methods=['GET'])
def about():
    return flask.render_template("about.html")
@app.route("/todo", methods=['POST'])
def todo():
    return "<p>To do: implement a webpage to respond to the post request</p>"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
