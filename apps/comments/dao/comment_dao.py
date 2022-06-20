import json
from json import JSONDecodeError
from apps.comments.dao.comment import Comment
from pprint import pprint as pp
from exceptions.data_exceptions import DataSourceError

POST_PATH = "../../../data/comments.json"


class CommentDAO:

    def __init__(self, path):
        self.path = path


    def _load_data(self):
        """ Загружает данные из файла для использования другими методами"""

        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                comments_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла {self.path}")

        list_of_comments = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_comments

    def _save_data(self, data):
        """ Перезаписывает переданные данные """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def get_all(self):
        """ Отдает полный список данных """
        data = self._load_data()
        return data


    def get_comments_by_post_id(self, post_id):
        """"Возвращает комментарии определенного поста"""

        if type(post_id) != int:
            raise TypeError("post_id must be int")

        comments = self._load_data()
        matching_comments = []
        for comment in comments:
            if post_id == comment.post_id:
                matching_comments.append(comment)

        return matching_comments


# dm = CommentDAO("../../../data/comments.json")
# pp(dm.get_comments_by_post_id(4))
