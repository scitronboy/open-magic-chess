from flask import Flask, redirect
from flask_socketio import SocketIO

import config as cfg

# The app is served as static files from the build directory:
app = Flask(__name__, static_url_path=cfg.APP_BASE_URL, static_folder=cfg.APP_BUILD_DIR)

socketio = SocketIO(app)

@app.route('/')
def redir_to_index():
    return redirect(cfg.APP_BASE_URL + '/index.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "404 Error. Please <a href='/'>return to the app</a>.", 404
    
@app.errorhandler(505)
def page_not_found(e):
    # note that we set the 505 status explicitly
    return "Something went wrong. Please try again.", 505
    
def start(logging_handler):
    app.logger.addHandler(logging_handler)
    socketio.run(app, host='0.0.0.0', port=80, use_reloader=False, debug=True)
