from flask import Flask
from api_routes import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
