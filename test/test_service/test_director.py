from unittest.mock import MagicMock
import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService
from setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name='name1')
    director_2 = Director(id=2, name='name2')
    director_3 = Director(id=3, name='name3')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock(return_value=director_1)
    director_dao.update = MagicMock(return_value=director_1)

    return director_dao


class TestDirectorsService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            'description': 'test',
            'rating': 777,
            'title': 'test',
            'trailer': 'test',
            'year': 7777,
            'genre_id': 777,
            'director_id': 777
        }
        director = self.director_service.create(director_d)
        assert director.id != None

    def test_delete(self):
        ret = self.director_service.delete(1)
        assert ret == None

    def test_udate(self):
        director_d = {
            'id': 7,
            'description': 'test2',
            'rating': 777,
            'title': 'test2',
            'trailer': 'test2',
            'year': 7777,
            'genre_id': 777,
            'director_id': 777
        }
        director = self.director_service.update(director_d)
        assert director != None
