import flask
app = flask.Flask('first_app')

@app.route('/')
def index():
  # choose template and fill blanks. get html
  html = flask.render_template('base.html',
                               title="hello flask")
  return html

app.run(host='0.0.0.0', port=80, debug=False)