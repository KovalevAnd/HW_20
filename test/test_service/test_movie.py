from unittest.mock import MagicMock
import pytest
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(id=1, title='title1', description='description1', trailer='trailer1', year=1991, rating=1)
    movie_2 = Movie(id=2, title='title2', description='description2', trailer='trailer2', year=1992, rating=2)
    movie_3 = Movie(id=3, title='title3', description='description3', trailer='trailer3', year=1993, rating=3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock(return_value=movie_1)
    movie_dao.update = MagicMock(return_value=movie_1)

    return movie_dao


class TestMoviesService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'description': 'test',
            'rating': 777,
            'title': 'test',
            'trailer': 'test',
            'year': 7777,
            'genre_id': 777,
            'director_id': 777
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def test_delete(self):
        ret = self.movie_service.delete(1)
        assert ret == None

    def test_udate(self):
        movie_d = {
            'id': 7,
            'description': 'test2',
            'rating': 777,
            'title': 'test2',
            'trailer': 'test2',
            'year': 7777,
            'genre_id': 777,
            'director_id': 777
        }
        movie = self.movie_service.update(movie_d)
        assert movie != None
