from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default="N/A")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post {self.id}"


@app.route("/", methods=["GET", "POST"])
def index():
    posts = Post.query.all()
    if request.method == "GET":
        return render_template("index.html", posts=posts)
    else:
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        new_post = Post(title=title, author=author, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("index"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
