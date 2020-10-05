import allure
import pytest
from base.logger import automation_logger, logger

test_case = "TestMovieWasUpdated"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("api_client")
@allure.description("""
    Functional Tests.
    1. Check that 
    """)
@pytest.mark.api
class TestMovieWasUpdated(object):

    @automation_logger(logger)
    def test_movie_was_updated(self, api_client):
        allure.step("Verify that movie was updated in last week.")

        res = api_client.get_movie_changes()
        assert res[0] is not None
        assert res[1].status_code == 200
        assert res[1].reason == "OK"

        logger.info(F"============ TEST CASE {test_case} / 1 PASSED ===========")
