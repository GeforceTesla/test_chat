from flask import Flask, request, jsonify

app = Flask(__name__)


def server_init():
    global chat_data
    chat_data = {}
    global count
    count = 0


def server_run():
    server_init()
    app.run(host='0.0.0.0', port=8888, debug=True)


@app.route("/", methods=['POST', 'GET'])
def basic_chat_history():
    global chat_data
    global count
    return_data = {}
    if request.method == "GET":
        if chat_data == {}:
            return_data["count"] = count
            return_data["id"] = "None"
            return_data["data"] = "No message yet"
            return jsonify(return_data)
        else:
            print 'return latest chat data'
            return_data = chat_data
            return_data["count"] = count
            return jsonify(return_data)
    elif request.method == "POST":
        print 'get the data and store'
        chat_data["id"] = request.form["id"]
        chat_data["data"] = request.form["data"]
        print count
        count += 1
        return "good"


if __name__ == "__main__":
    server_run()
