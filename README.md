Introduction
============

It's an assistant app for Yuque in Slack. 

Requirements
============

* Python: 3.7.2 
* pip
* virtualenv
* Docker (optional)

How to Use
===========

***Config*** 

Replace `SLACK_WEBHOOK` in `config.temp.py` , you can check it out from your Slack App Setting. 

Replace `SLACK_CLIENT_ID` in `config.temp.py` , you can check it out from your Slack App Setting. 

Replace `SLACK_CLIENT_SECRET` in `config.temp.py` , you can check it out from your Slack App Setting. 

***Setup***

`http://YOUR_URL/slack-webhook` : Copy and paste this url into yuque webhook url field. Keep getting updates from Yuque repo or document. 

`http://YOUR_URL/auth-test` : You can test Slack Oauth process with these relative functions.`

***Relative documents***

[Slack API](https://api.slack.com/slack-apps/)

[语雀 API](https://www.yuque.com/yuque/developer)

Development
============

***Develop***

> git clone 

> virtualenv env 

> source env/bin/active 

> cd app/

> pip install -r requirements.txt

> sh dev.sh

***Deploy***

> start: make start-pro

> stop: make stop-pro 

> copy this `http://your_domain:5000/slack-webhook` url into your Yuque webhook config.

Roadmap
=========

* ~~0.1.x: Integrate with Yuque & Slack webhook~~
* ~~0.2.1: Get Oauth info from Slack~~ 
* 0.2.2: Config Database into this app allows users to store their hooks  
* 0.3.x: Distribution as a simple assistant app in Slack
* 0.4.x: Support Slack Commands 
