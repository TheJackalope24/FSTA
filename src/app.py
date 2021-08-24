from flask import Flask

# This is general Flask configuration. Note that you do not typically create several instances of
# the imported Flask class and that we are only doing it for today's demo.

# __name__ is a built-in variable which evaluates to the name of the current module. It is often used
# to determine whether the current script is being run on its own or being imported somewhere else. If
# a module is being directly run, __name__ evaluates to __main__.

flask_app = Flask(__name__, template_folder="static/templates", static_folder="static")
