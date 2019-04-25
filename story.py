from flask import Flask, request, Response
import json

import pandas as pd

app = Flask(__name__)

columns = ['title', 'text', 'current_user', 'state']
df = pd.DataFrame(columns=columns)

@app.route('/story/start', methods=["POST"])
def start_story():
	if request.headers['Content-Type'] == 'application/json':
		arguments = request.get_json()
		title = arguments.get("title")
		text = arguments.get("text")
		current_user = arguments.get("current_user")
		state = arguments.get("state")

	df.loc[len(df)] = [title, text, current_user, state]
		
	resp = Response(json.dumps({ "title": title }), status=201, mimetype='application/json')
	return resp
	

@app.route('/story/list', methods=["GET"])
def list_stories():
	resp = Response(json.dumps(df.to_dict()), status=200, mimetype='application/json')
	return resp

# @app.route('/story/<title>')

# @app.route('story/<title>/edit')

# @app.route('story/<title>/end')

# @app.route('story/<title>/leave')