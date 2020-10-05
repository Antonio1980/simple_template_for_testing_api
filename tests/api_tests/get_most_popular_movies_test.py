import allure
import pytest
from base.logger import automation_logger, logger

test_case = "TestMostPopularMovies"


@pytest.mark.incremental
@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("api_client")
@allure.description("""
    Functional Tests.
    1. Check that request get_most_popular_movies is returned 200 status code.
    2. Check that client can request 50 most popular movies.
    3. Check that for every movie returned correct data type.
    """)
@pytest.mark.api
class TestMostPopularMovies(object):
    _response = None

    @automation_logger(logger)
    def test_get_most_popular_movies(self, api_client):
        allure.step("Verify that status code is 200 OK.")
        res = api_client.get_most_popular_movies()
        assert res[0] is not None
        assert res[1].status_code == 200
        assert res[1].reason == "OK"

        logger.info(F"============ TEST CASE {test_case} / 1 PASSED ===========")

    @automation_logger(logger)
    def test_get_first_50_most_popular_movies(self, api_client):
        allure.step("Verify that client able to get 50 most popular movies")
        _response1 = api_client.get_most_popular_movies()[0]["results"]
        _response2 = api_client.get_most_popular_movies(page=2)[0]["results"]
        _response3 = api_client.get_most_popular_movies(page=3)[0]["results"][:10]

        TestMostPopularMovies._response = _response1 + _response2 + _response3

        assert len(TestMostPopularMovies._response) == 50

        logger.info(F"============ TEST CASE {test_case} / 2 PASSED ===========")

    @automation_logger(logger)
    def test_data_type_for_each_movie(self, api_client):
        allure.step("Verify that for each movie returned correct data type.")

        for item in TestMostPopularMovies._response:
            res = api_client.get_movie_by_id(str(item["id"]))[0]
            assert res["original_title"] == item["original_title"]
            assert res["adult"] == item["adult"]
            assert res["backdrop_path"] == item["backdrop_path"]

        logger.info(F"============ TEST CASE {test_case} / 3 PASSED ===========")

