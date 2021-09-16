import requests 
import config
from flask import Flask, request, jsonify, redirect, json 

def get_auth_info(code, state):
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


def post_to_slack(channel, doc_title, doc_slug, repo_title, repo_slug, login_group):
    if channel in config.CHANNELS:
        slack_webhook_url = config.CHANNELS[channel]
        msg_text = " *Document:* <https://www.yuque.com/%s/%s/%s|%s> has been updated :star: " %(login_group, repo_slug, doc_slug, doc_title) 
        repo_text = "Repo: %s" %( repo_title )
        print(msg_text)
        req_data = {
                    "text": "%s ✍️" %(doc_title), 
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
    else:
        print('can not find channel in config')
        return None
