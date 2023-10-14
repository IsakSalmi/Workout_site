from flask import Flask, render_template, request, Response

app = Flask(__name__, template_folder="Templates")


@app.route('/', methods=['GET'])
def index_get():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(host='', port=80, debug=True)
