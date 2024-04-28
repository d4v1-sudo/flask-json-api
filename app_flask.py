from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)

# Simulating a simple database
data_store = {'key': '1', 'value': 'coin'}

@app.route('/env', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if not data:
            raise BadRequest(description='Invalid JSON data')

        # Validate data as needed
        if 'key' not in data or 'value' not in data:
            raise BadRequest(description='Key and value are required fields')

        key = data['key']
        value = data['value']

        # Store the data somewhere (in this example, in memory)
        data_store[key] = value

        # Print the received data
        print(f'Received Data: {data}')

        return "Data received successfully", 201  # HTTP status code 201 for successful creation
    except BadRequest as e:
        return str(e), 400  # HTTP status code 400 for a bad request
    except Exception as e:
        return str(e), 500  # HTTP status code 500 for an internal server error

@app.route('/get/<key>', methods=['GET'])
def get_data(key):
    try:
        if key in data_store:
            value = data_store[key]
            return jsonify({key: value})
        else:
            raise NotFound(description=f'Key "{key}" not found')
    except NotFound as e:
        return str(e), 404  # 404 code for resource not found
    except Exception as e:
        return str(e), 500  # 500 code for internal server error

@app.route('/page', methods=['GET'])
def show_page():
    try:
        return render_template('index.html')  # Render the HTML file
    except Exception as e:
        return str(e), 500

@app.route('/chat', methods=['POST'])
def exchange_message():
    try:
        data = request.get_json()
        if not data:
            raise BadRequest(description='Invalid JSON data')

        message = data.get('message')
        if message:
            print(f'Received Message: {message}')
            return "Message received successfully", 200
        else:
            raise BadRequest(description='Message not found in JSON')
    except BadRequest as e:
        return str(e), 400  # HTTP status code 400 for a bad request
    except Exception as e:
        return str(e), 500  # HTTP status code 500 for an internal server error

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
