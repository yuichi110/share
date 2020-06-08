import datetime, flask, json, pickle
app = flask.Flask('first_app')

try:
  with open('post_data.pickle', 'rb') as fin:
    POST_DATA = pickle.load(fin)
except:
  POST_DATA = []

def write():
  with open('post_data.pickle', 'wb') as fout:
    pickle.dump(POST_DATA, fout)


INDEX_HTML = '''
<ul>
  {}
</ul>
'''

@app.route('/')
def index():
  lis = ''
  for li in POST_DATA:
    timestamp = li['timestamp']
    text = li['text']
    lis += f'<li>  {timestamp} - {text}</li>\n'
  content = INDEX_HTML.format(lis)
  html = flask.render_template('base.html', title="Home",
    home="active", post="", content=content)
  return html


POST_HTML = '''
<form action="/post" method="POST">
  <div class="form-group">
    <label for="input-post">Message</label>
    <input type="text" name="text" class="form-control" id="input-post">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
'''

@app.route('/post', methods=['GET', 'POST'])
def post():
  if flask.request.method == 'POST':
    POST_DATA.append({
      'timestamp': datetime.datetime.now().isoformat(),
      'text': flask.request.form['text']
    })
    write()

  html = flask.render_template('base.html', title="Post",
    home="", post="active", content=POST_HTML)
  return html

app.run(host='0.0.0.0', port=80, debug=False)