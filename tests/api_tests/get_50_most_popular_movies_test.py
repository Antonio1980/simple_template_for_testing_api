import allure
import pytest
from base.logger import automation_logger, logger

test_case = "TestFiftyMostPopularMovies"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    Functional Tests.
    1. Check that client can request 50 most popular movies.
    """)
@pytest.mark.api
class TestFiftyMostPopularMovies(object):

    @automation_logger(logger)
    def test_get_first_50_most_popular_movies(self, api_client):
        allure.step("Verify that client able to get 50 most popular movies")
        _response1 = api_client.get_most_popular_movies()[0]["results"]
        _response2 = api_client.get_most_popular_movies(page=2)[0]["results"]
        _response3 = api_client.get_most_popular_movies(page=3)[0]["results"][:10]

        _response = _response1 + _response2 + _response3

        assert len(_response) == 50

        logger.info(F"============ TEST CASE {test_case} / 2 PASSED ===========")
