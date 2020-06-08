import flask
app = flask.Flask('first_app')

@app.route('/')
def index():
  html = flask.render_template('base.html', title="Home",
    home="active", post="", content="Home Page")
  return html

@app.route('/post')
def post():
  html = flask.render_template('base.html', title="Post",
    home="", post="active", content="Post Page")
  return html

app.run(host='0.0.0.0', port=80, debug=True)