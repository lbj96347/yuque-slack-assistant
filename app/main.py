import requests 
import config
import slackapp
import yuqueapp
from flask import Flask, request, jsonify, redirect, json 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey! Here is Yuque-Slack App.'

@app.route('/post-to-slack')
def test():
    slackapp.post_to_slack("Test Document Title", 
            "test", 
            "Test Repo", 
            "product", 
            "kiwi")
    return 'post to slack'

@app.route('/slack-webhook', methods = ['POST'])
def slack_hook():
    update_data = request.get_data()
    info = yuqueapp.extract_yuque_update(update_data)
    slackapp.post_to_slack( info['doc_title'], 
            info['doc_slug'], 
            info['repo_title'], 
            info['repo_slug'] , 
            info['login_group'])
    return 'slack hook info' 

@app.route('/auth_test')
def auth():
    # can get the code from second time request 
    code = request.args.get('code')
    state = request.args.get('state')
    slackapp.get_auth_info(code, state)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
