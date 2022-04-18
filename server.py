
from flask_app import app
from flask_app.controllers import controller_dojos, controller_ninjas


# This needs to stay at the bottom
if __name__ == "__main__":
    app.run(debug=True, port=8000)
