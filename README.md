Introduction
============

It's an assistant app for Yuque in Slack. 

Requirements
============

* Python: 3.7.2 
* pip
* Docker (optional)

How to Use
===========

***Config*** 

Replace `SLACK_WEBHOOK` in `config.temp.py` , you can check it out from your Slack App Setting. 

***Develop***

> git clone 

> cd app/

> virtualenv env 

> source /env/bin/active 

> pip install -r requirements.txt

> FLASK_APP=app.py flask run

***Deploy***

> start: make start-pro

> stop: make stop-pro 

> copy this `http://your_domain:5000/slack-webhook` url into your Yuque webhook config.

Features
=========

null 

Roadmap
=========

* 0.1.x: Integrate with Yuque & Slack webhook
* 0.2.x: Production mode configure
* 0.3.x: Slack commands 
