from unittest.mock import MagicMock
import pytest

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService
from setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name='name1')
    genre_2 = Genre(id=2, name='name2')
    genre_3 = Genre(id=3, name='name3')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock(return_value=genre_1)
    genre_dao.update = MagicMock(return_value=genre_1)

    return genre_dao


class TestDirectorsService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            'description': 'test',
            'rating': 777,
            'title': 'test',
            'trailer': 'test',
            'year': 7777,
            'genre_id': 777,
            'director_id': 777
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id != None

    def test_delete(self):
        ret = self.genre_service.delete(1)
        assert ret == None

    def test_udate(self):
        genre_d = {
            'id': 7,
            'description': 'test2',
            'rating': 777,
            'title': 'test2',
            'trailer': 'test2',
            'year': 7777,
            'genre_id': 777,
            'director_id': 777
        }
        genre = self.genre_service.update(genre_d)
        assert genre != None
