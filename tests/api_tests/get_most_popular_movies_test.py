import allure
import pytest
from base.logger import automation_logger, logger

test_case = "TestMostPopularMovies"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    Functional Tests.
    1. Check that request get_most_popular_movies is returned 200 status code.
    """)
@pytest.mark.api
class TestMostPopularMovies(object):

    @automation_logger(logger)
    def test_get_most_popular_movies(self, api_client):
        allure.step("Verify that status code is 200 OK.")
        res = api_client.get_most_popular_movies()
        assert res[0] is not None
        assert res[1].status_code == 200
        assert res[1].reason == "OK"

        logger.info(F"============ TEST CASE {test_case} / 1 PASSED ===========")
