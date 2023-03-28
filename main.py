from flask import Flask, jsonify, request,send_file

app = Flask(__name__)
user_name = 'John Elstad'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_name', methods = ['GET'])
def get_name():
    return user_name

@app.route('/set_name', methods = ['PUSH'])
def set_name():
        name = request.args.get('name')
        if name is None:
            text = "No name given"
        else:
            text = "Hello: " + name
            user_name = name
        return text
if __name__ == '__main__':
    app.run(debug=True, port = 8101)
