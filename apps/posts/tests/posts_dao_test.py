from apps.posts.dao.post_dao import PostDAO
import pytest

from apps.posts.dao.posts import Post
from apps.views import posts_dao


def check_fields(post):
    fields = ["poster_name",
                  "poster_avatar",
                  "pic",
                  "content",
                  "views_count",
                  "likes_count",
                  "pk"]
    for field in fields:
        assert hasattr(post,field), f"Нет поля {field}"

class TestPostDAO:

    @pytest.fixture
    def posts_dao(self):
        posts_dao_instance = PostDAO("C:/Users/Admin/PycharmProjects/coursework3_source/apps/posts/tests/post_mock.json")
        return posts_dao_instance

    """ Функция получения всех постов"""

    def test_get_all_types(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_all()
        assert type(posts) == list, "возвращается не список"

        post = posts_dao.get_all()[0]
        assert type(post) == Post, "возвращается не список постов"

        posts = posts_dao.get_all()
        assert len(posts) > 0, "возвращается пуcтой список"
        # assert set(posts.keys()) == keys_should_be, "неверный список ключей"

    def test_get_all_fields(self):
        # posts = posts_dao.get_all()
        post = posts_dao.get_all()[0]
        check_fields(post)

    """ Тестируем функцию получения поста по pk"""

    def test_get_by_pk_fields(self, posts_dao):
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == Post, "возвращается не список постов"


    def test_get_by_pk_types(self, posts_dao):
        post = posts_dao.get_post_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, posts_dao):
        post = posts_dao.get_post_by_pk(744)
        assert post is None, "Должно быть None для несуществующего pk"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, posts_dao, pk):
        post = posts_dao.get_post_by_pk(pk)
        assert post.pk == pk, f"Неверный post.pk по pk"

    """ Функция получения  постов по ключевому слову"""

    def test_search_for_posts_by_substring_types(self, posts_dao):
        posts = posts_dao.search_for_posts_by_name("ага")
        assert type(posts) == list, "возвращается не список постов"
        post = posts_dao.get_all()[0]
        assert type(post) == Post, "неверный тип для одного поста"

    def test_search_for_posts_by_substring_fields(self, posts_dao):
        posts = posts_dao.search_for_posts_by_name("ага")
        post = posts_dao.get_all()[0]
        check_fields(post)

    def test_search_for_posts_not_found(self, posts_dao):
        posts = posts_dao.search_for_posts_by_name("ghjd78996")
        assert posts == [], "Должен быть пустой список для несуществующего ключевого слова"

