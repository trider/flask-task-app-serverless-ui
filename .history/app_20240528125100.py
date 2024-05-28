from flask import Flask, redirect,jsonify
from markupsafe import escape
from flask_swagger_ui import get_swaggerui_blueprint
from api import api


SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Flask Task API'
    }
)



app = Flask(__name__)
app.register_blueprint(api.bp)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def index():
     return jsonify(message='Hello from root!')
    
    # return redirect("https://u767k4g1u6.execute-api.us-east-1.amazonaws.com/swagger/")


if __name__ == "__main__":
  print('****************************************')
  print('flask-task-app: Ver', '0.1.2')
  print('****************************************\n')
  # app.run(host='0.0.0.0', port=5000, debug=True)
  app.debug = True
  app.run()









# # from flask import Flask, jsonify, make_response

# # app = Flask(__name__)


# # @app.route("/")
# # def hello_from_root():
# #     return jsonify(message='Hello from root!')


# # @app.route("/hello")
# # def hello():
# #     return jsonify(message='Hello from path!')


# # @app.errorhandler(404)
# # def resource_not_found(e):
# #     return make_response(jsonify(error='Not found!'), 404)
