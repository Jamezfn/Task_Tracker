from flask import Flask
from app.routes.auth import auth_routes

app = Flask(__name__)
# initiallizing database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"

@app.route('/')
def hello_world():
    return "<p>Hello, World welcome!</p>"

app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(debug=True)