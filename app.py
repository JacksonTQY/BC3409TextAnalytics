#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import sqlite3
from textblob import TextBlob


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        t = request.form.get('text')
        print(t)
        r = TextBlob(t).sentiment
        return render_template("index.html", results=r)
    else:
        return render_template("index.html", results="GET")


if __name__ == "__main__":
    app.run()


# In[ ]:




