from flask import Flask, render_template, request, Response

import DB

app = Flask(__name__, template_folder="Templates")


@app.route('/', methods=['GET'])
def index_get():
    return render_template("log_in.html")


@app.route('/', methods=['POST'])
def indexPost():
    answer = str(request.json).split()
    if request.method == "POST" and DB.check_user(answer[0], answer[1]):
        return Response("OK", 200)
    else:
        return Response("invalid", 400)


@app.route('/create_account', methods=['GET'])
def createAcc():
    return render_template("create_account.html")


@app.route('/log_in', methods=['GET'])
def getLogin():
    return render_template("log_in.html")


if __name__ == '__main__':
    app.run(host='', port=80, debug=True)
