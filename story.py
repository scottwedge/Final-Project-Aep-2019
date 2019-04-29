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
def list_stories_titles():
	resp = Response(df['title'].to_json(), status=200, mimetype='application/json')
	return resp

@app.route('/story/<title>')
def display_story(title):
	row = df.loc[df['title'] == title]
	resp = Response(row.to_json(), status=200, mimetype='application/json')
	return resp


@app.route('/story/<title>/edit', methods=["PUT"])
def edit_story(title):

	row = df.loc[df['title'] == title]

	if request.headers['Content-Type'] == 'application/json':
		arguments = request.get_json()
		title = arguments.get("title")
		new_text = arguments.get("new_text")
		current_user = arguments.get("current_user")
		state = arguments.get("state")

	old_text = row['text']
	text = old_text + new_text
	df.loc[df.title==title, ['text', 'current_user', 'state']] = [text, current_user, state]
	row = df.loc[df['title'] == title]
	
	resp = Response(row.to_json(), status=201, mimetype='application/json')
	return resp

# @app.route('/story/<title>/end', methods=["PUT"])


# @app.route('/story/<title>/leave')