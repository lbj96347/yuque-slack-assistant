import requests 
import config
from flask import Flask, request, jsonify, json 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey! Here is Yuque-Slack App.'

@app.route('/slack-webhook', methods = ['POST'])
def slack_hook():
    update_data = request.get_data()
    info = json.loads(update_data) 
    doc_title = info['data']['title']
    doc_slug = info['data']['slug']
    repo_title = info['data']['book']['name']
    repo_slug = info['data']['book']['slug']
    # print_str = "title: %s \n  , doc_slug: %s \n , repo_title: %s \n , repo_slug: %s \n" %(doc_title, doc_slug, repo_title, repo_slug)
    print(doc_title, doc_slug, repo_title, repo_slug)
    post_to_slack( doc_title, doc_slug, repo_title, repo_slug )
    return 'slack hook info' 

@app.route('/post-to-slack')
def test():
    post_to_slack("Test Document", "tsmv86", "Mesh 产品内部文档", "product")
    return 'post to slack'

def post_to_slack(doc_title, doc_slug, repo_title, repo_slug):
    slack_webhook_url = SLACK_WEBHOOK
    msg_text = " *Document:* <https://www.yuque.com/kiwi/%s/%s|%s> has been updated :star: " %(repo_slug, doc_slug, doc_title) 
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

