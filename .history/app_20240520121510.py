from flask import Flask
from markupsafe import escape

from api import api



app = Flask(__name__)
app.register_blueprint(api.bp)

@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
  print('****************************************')
  print('flask-task-app: Ver', '0.1.1')
  print('****************************************\n')
  # app.run(host='0.0.0.0', port=5000, debug=True)
  app.debug = True
  app.run()









# from flask import Flask, jsonify, make_response

# app = Flask(__name__)


# @app.route("/")
# def hello_from_root():
#     return jsonify(message='Hello from root!')


# @app.route("/hello")
# def hello():
#     return jsonify(message='Hello from path!')


# @app.errorhandler(404)
# def resource_not_found(e):
#     return make_response(jsonify(error='Not found!'), 404)
