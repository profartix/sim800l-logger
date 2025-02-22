from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log():
    message = request.args.get('text', 'No message')
    print(f"Получен лог: {message}")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
