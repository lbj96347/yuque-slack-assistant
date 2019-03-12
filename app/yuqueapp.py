import requests 
import config
from flask import Flask, request, jsonify, redirect, json 

def extract_yuque_update(update_data):
    info = json.loads(update_data) 
    doc_title = info['data']['title']
    doc_slug = info['data']['slug']
    repo_title = info['data']['book']['name']
    repo_slug = info['data']['book']['slug']
    login_group = info['data']['user']['login']
    print(doc_title, 
            doc_slug, 
            repo_title, 
            repo_slug, 
            login_group)
    return {"doc_title": doc_title, 
            "doc_slug": doc_slug, 
            "repo_title": repo_title,
            "repo_slug": repo_slug,
            "login_group": login_group}
