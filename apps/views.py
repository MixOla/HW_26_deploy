import logging
from config import  DATA_PATH_POSTS, DATA_PATH_COMMENTS
from flask import Blueprint, render_template, request, current_app, jsonify, abort, redirect

from apps.posts.dao.post_dao import PostDAO
from apps.comments.dao.comment_dao import CommentDAO


# Создаем блупринт
post_blueprint = Blueprint("post_blueprint", __name__, template_folder="../../templates")

posts_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentDAO(DATA_PATH_COMMENTS)

logger = logging.getLogger("basic")


@post_blueprint.route("/")
def main_page():
    posts = posts_dao.get_all()
    return render_template("index.html", posts=posts)


@post_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    post = posts_dao.get_post_by_pk(post_id)
    comments = comments_dao.get_comments_by_post_id(post_id)
    len_comments = len(comments)
    tags_list = posts_dao.search_tags_in_post(post_id)
    if post is None:
        abort(404)

    return render_template("post.html", post=post, comments=comments, len_comments=len_comments, tags_list=tags_list)


@post_blueprint.route("/users/<user_name>")
def user_name_page(user_name):
    posts = posts_dao.search_for_posts_by_name(user_name)

    if not posts:
        abort(404, "Такого пользователя не существует")

    return render_template("user-feed.html", posts=posts)

@post_blueprint.route("/search/")
def page_posts_search():
    """ Возвращает результаты поиска"""
    query = request.args.get("s", "")

    if query == "":
        posts = []
        len_posts = len(posts)
    else:
        posts = posts_dao.search_for_posts(query)[:10]
        len_posts = len(posts)

    return render_template("search.html", posts=posts, query=query, len_posts=len_posts)


@post_blueprint.route("/tag/<tag_name>")
def tag_name_page(tag_name):
    posts = posts_dao.get_posts_by_tag(tag_name)
    return render_template("tag.html", posts=posts, tag_name=tag_name)


# @post_blueprint.route("/bookmarks/add/<postid>")
# def bookmarks_page(postid):
#     posts = posts_dao.add(postid)
#     return redirect("/", code=302)


