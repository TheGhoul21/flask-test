import click;
from flask import Flask, render_template

app = Flask(__name__, static_folder='templates/assets')

@app.route("/")
def index():
    return render_template('index.html', username= 'Mario')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/assets/<path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run()
