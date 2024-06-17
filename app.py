from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap5


from markupsafe import escape
from api import api
from tasks import hello, login, tasks



app = Flask(__name__)
app.register_blueprint(api.bp)
app.register_blueprint(hello.bp)
app.register_blueprint(login.bp)
app.register_blueprint(tasks.bp)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
bootstrap = Bootstrap5(app)




@app.route('/')
def index():
    return redirect("/login")


  
    

if __name__ == "__main__":
  print('****************************************')
  print('flask-task-app: Ver', '0.1.3')
  print('****************************************\n')
  # app.run(host='0.0.0.0', port=5001, debug=True)
  # app.debug = True
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
