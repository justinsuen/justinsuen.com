from flask import Flask
from flask import render_template

import info
from blog import construct_blog_posts
from flaskext.markdown import Markdown

application = Flask(__name__)

# Enabling markdown allows us to write prettier blog posts
Markdown(application)

# These are the arguments passed into the templates that will be used with every rendered page. They
# take care of Search Engine Optimization and nav-bar stuff and can be
# edited in info.py.
layout_args = {
    "meta": info.meta,
    "navigation": info.nav,
}


@application.route("/")
@application.route("/index")
@application.route("/index.html")
def index():
  return render_template("index.html",  about=info.about, projects=info.projects, **layout_args)


@application.route("/blog")
@application.route("/blog.html")
def blog():
  path = 'static/assets/posts/'
  return render_template("blog.html", blog_posts=construct_blog_posts(path), **layout_args)


@application.route("/resume")
@application.route("/resume.pdf")
def resume():
  return application.send_static_file("assets/resume.pdf")

if __name__ == "__main__":
  application.debug = True
  application.run()
