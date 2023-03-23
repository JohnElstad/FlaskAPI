from flask import flask, jsonify, request, send_file
app = Flask()

@app.route('/my-first-api',methods = ['GET'])
def hello():
        name = request.args.get('name')
        if name is none:
            text = "No name"
        else:
            text = "Hello: " + name
        return text

if __name__ == '__main__':
    app.run(debug=True, port = 8101)
