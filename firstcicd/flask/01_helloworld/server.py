import flask

# create flask app
app = flask.Flask('first_app')

# add page function to app witu url "/hello"
@app.route('/hello')
def index():
  return 'hello flask'

# accept access at port 80 from any source
app.run(host='0.0.0.0', port=80, debug=False)