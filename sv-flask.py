import json
from flask import Flask, jsonify, request, session, g, redirect, url_for, abort, \
             render_template, flash
import rawmodels

app = Flask(__name__)
app.debug = True

@app.route("/")
def get_all():
    Commits = rawmodels.Commits()
    commits = Commits.getAll()
    return render_template("base.html", commits=json.dumps(commits))

if __name__ == "__main__":
    app.run()
