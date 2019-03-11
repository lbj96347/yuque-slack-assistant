import requests 
import config
from flask import Flask, request, jsonify, redirect, json 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey! Here is Yuque-Slack App.'

@app.route('/post-to-slack')
def test():
    post_to_slack("Test Document Title", "test", "Test Repo", "product", "kiwi")
    return 'post to slack'

@app.route('/slack-webhook', methods = ['POST'])
def slack_hook():
    update_data = request.get_data()
    info = json.loads(update_data) 
    doc_title = info['data']['title']
    doc_slug = info['data']['slug']
    repo_title = info['data']['book']['name']
    repo_slug = info['data']['book']['slug']
    login_group = info['data']['user']['login']
    # print_str = "title: %s \n  , doc_slug: %s \n , repo_title: %s \n , repo_slug: %s \n" %(doc_title, doc_slug, repo_title, repo_slug)
    print(doc_title, doc_slug, repo_title, repo_slug, login_group)
    post_to_slack( doc_title, doc_slug, repo_title, repo_slug , login_group)
    return 'slack hook info' 

@app.route('/auth_test')
def auth():
    # can get the code from second time request 
    code = request.args.get('code')
    state = request.args.get('state')
    if not code and not state :
        request_url = "https://slack.com/oauth/authorize?client_id=%s&scope=incoming-webhook" %(config.SLACK_CLIENT_ID) 
        return redirect(request_url)
    else:
        print("request access token")
        obtain_access_token = "https://slack.com/api/oauth.access?client_id=%s&client_secret=%s&code=%s" %(config.SLACK_CLIENT_ID, config.SLACK_CLIENT_SECRET, code) 
        payload = requests.get(
            obtain_access_token
        )
        # get slack hooks url 
        # the next step is cache slack hooks url and binding with yuque hook url
        print(json.loads(payload.text))
        return code  

def post_to_slack(doc_title, doc_slug, repo_title, repo_slug, login_group):
    slack_webhook_url = config.SLACK_WEBHOOK
    msg_text = " *Document:* <https://www.yuque.com/%s/%s/%s|%s> has been updated :star: " %(login_group, repo_slug, doc_slug, doc_title) 
    repo_text = "Repo: %s" %( repo_title )
    print(msg_text)
    req_data = {
        "blocks": [
            {
                "type": "divider"
            },{
              "type": "section",
              "text": {
                "type": "mrkdwn",
                "text": msg_text 
              }
            },{
		"type": "context",
		"elements": [
			{
                            "type": "plain_text",
                            "text": repo_text ,
                            "emoji": True 
			}
		]
	    }
        ]
    }
    requests.post(
        slack_webhook_url,
        json=req_data
    )

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
