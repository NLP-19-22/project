
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import json

import module.GoogleService as gs
from module.extractWord.keyword_extraction import extract

app = Flask(__name__)

def query_getLinks(originalContent):
    query = extract(str(originalContent))
    links = gs.getLinks(query)
    print(links)
    results_list = []
    i = 0
    for link in links:
        title = gs.getTitle(link)
        text = gs.extract_text(link)
        results_list.append({
            "id": i,
            "link": link,
            "title": title,
            "text": text,
            "score": 10-i,
        })
        i += 1
    return json.dumps(results_list)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        return query_getLinks(request.form.get("originalContent", ""))
    if request.method == "GET":
        return query_getLinks(request.args.get("originalContent", ""))
    return "Only GET and POST methods are allowed for this endpoint"

if __name__ == '__main__':
    app.run(debug=True)