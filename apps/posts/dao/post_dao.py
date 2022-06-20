import json
import os
from json import JSONDecodeError
from apps.posts.dao.posts import Post
from pprint import pprint as pp
from exceptions.data_exceptions import DataSourceError

# POST_PATH = "coursework3_source/data/data.json"
POST_PATH = os.path.join("data", "data.json")


class PostDAO:

    def __init__(self, path):
        self.path = path


    def _load_data(self):
        """ Загружает данные из файла для использования другими методами"""

        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла {self.path}")

        list_of_posts = [Post(**post_data) for post_data in posts_data]

        return list_of_posts


    def _save_data(self, data):
        """ Перезаписывает переданные данные """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)


    def get_all(self):
        """ Отдает полный список данных """
        data = self._load_data()
        return data


    def search_for_posts(self, substring):
        """"Возвращает список постов по ключевому слову """
        if type(substring) != str:
            raise TypeError("Substring must be str")

        posts = self._load_data()
        substring = substring.lower()

        matching_posts = [post for post in posts if substring in post.content.lower()]
        return matching_posts


    def get_post_by_pk(self, pk):
        """ Возвращает один пост по его идентификатору """
        if type(pk) != int:
            raise TypeError("pk must be int")

        posts = self._load_data()
        for post in posts:
            if pk == post.pk:
                return post


    def search_for_posts_by_name(self, user_name):
        """Возвращает список постов по имени автора поста """
        if type(user_name) != str:
            raise TypeError("user_name must be str")

        posts = self._load_data()
        user_name = user_name.lower()

        matching_posts = [post for post in posts if user_name in post.poster_name.lower()]
        return matching_posts


    def search_tags_in_post(self, pk):
        """ Функция возвращает список тегов одного поста"""

        # if type(tag_name) != dict:
        #     raise TypeError("tag_name must be str"
        post = self.get_post_by_pk(pk)
        content = post.content.split(" ")
        res_list_of_tags = [word[1:] for word in content if word[0] == "#"]
        return res_list_of_tags


    def get_posts_by_tag(self, tag):
        """ Функция возвращает список постов с одинаковыми тегами """
        posts = self._load_data()
        matching_posts = []
        for post in posts:
            if tag in post.content.split(" "):
                matching_posts.append(post)
        return matching_posts
    #
    #
    # def add(self, postid):
    #     """"Добавляет в закладки пост"""
    #     if type(postid) != int:
    #         raise TypeError("Int expected for adding post")
    #
    #     postid_res = self.get_post_by_pk(postid)
    #     with open('bookmarks.json', 'w', encoding='utf-8') as file:
    #         res = json.dump(postid_res, file)
    #         return res
