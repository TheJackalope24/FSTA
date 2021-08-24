from src.app import flask_app
import src.controller.user_controller

if __name__=='__main__':
    flask_app.run(debug=True)
