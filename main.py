import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Универсальная функция добавления CORS-заголовков
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = (
        'x-test,ngrok-skip-browser-warning,Content-Type,Accept,Access-Control-Allow-Headers'
    )
    response.headers['Content-Type'] = 'application/json'
    return response

# task 5
app = Flask(__name__)

@app.route('/login/', methods=['GET'])
def get_login():
    return '45cf3a7d-a058-4ede-a03c-2c98a130021d'

@app.route('/hour/', methods=['GET'])
def get_hour():
    return datetime.now(ZoneInfo('Europe/Moscow')).strftime("%H")




@app.route('/result4/', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def result4():
    # Обработка preflight-запроса
    if request.method == 'OPTIONS':
        return add_cors_headers(make_response())

    # Получаем заголовок x-test
    x_test = request.headers.get('x-test')

    # Получаем тело запроса как текст
    body = request.get_data(as_text=True)

    response_data = {
        "message": "45cf3a7d-a058-4ede-a03c-2c98a130021d",
        "x-result": x_test,
        "x-body": body
    }

    response = make_response(jsonify(response_data))
    return add_cors_headers(response)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)