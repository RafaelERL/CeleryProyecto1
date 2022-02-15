from celery import app
import json

@app.task
def check():
    print("I am checking your stuff")