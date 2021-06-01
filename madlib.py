from flask import Flask
import requests
import logging
import random
import json


app = Flask(__name__)

@app.route('/__health')
def health_check():
    return "OK", 200

@app.route('/')
def hello():
    return "hello rakshitha", 200

@app.route('/madlib/')
def getMadlib():
    try:
        story = makeStory()
        if story:
            # print(story)
            return story

    except Exception as e:
        return "Record not found", 400


def getTemplate():
    template = 'It was a {0}<a> day. I went downstairs to see if I could {1}<v> dinner. I asked, "Does the stew need fresh {2}<n>?"'
    fillers =["adjective", "verb", "noun"]
    return template, fillers
# get noun, verb adjective
def getFillers(filler):
    try:
        url = "https://reminiscent-steady-albertosaurus.glitch.me/{0}".format(filler)

        r = requests.get(url)
        if r.status_code ==200:
            # print(r.json())
            return r.json()
        else:
            raise Exception
    except Exception as err:
        # logging.info("Error not able to fetch an adjective")
        print("Error not able to fetch an adjective")
        return None


def makeStory():
    try:
        template , fillers = getTemplate()
        # print(template)
        words=[]
        for fill in fillers:
            madword = getFillers(fill)
            if not madword:
                print("cant generate error ")
                return None
            words.append(madword)

        # print(template.format(*words))
        return template.format(*words)

    except Exception as err:
        # logging.info("Error not able to fetch an adjective")
        return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)