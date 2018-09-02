from flask import Flask,jsonify,request,logging
from services.servicenow import servicenow

app = Flask(__name__)
app.register_blueprint(servicenow,url_prefix='/api/now')
app.debug = True
log = logging.create_logger(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
