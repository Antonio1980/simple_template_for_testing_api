import allure
import pytest
from base.logger import automation_logger, logger

test_case = "TestMovieWasUpdated"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    Functional Tests.
    1. Check that 
    """)
@pytest.mark.api
class TestMovieWasUpdated(object):

    @automation_logger(logger)
    def test_movie_was_updated(self, api_client, fifty_most_popular_movies):
        allure.step("Verify that movie was updated in last week.")
        end_date, start_date = "2020-10-06", "2020-10-01"
        res = api_client.get_movie_changes(end_date, start_date)
        assert res[0] is not None
        assert res[1].status_code == 200
        assert res[1].reason == "OK"

        updates = res[0]["results"]

        for item in fifty_most_popular_movies:
            for dict_ in updates:
                if item["id"] == dict_["id"]:
                    logger.info(f"This movie {item['id']} is updated in last week.")
                    dict_["test"] = True
                    break
                else:
                    if "test" in dict_.keys() and dict_["test"] is True:
                        pass
                    else:
                        dict_["test"] = False

        for dict_ in updates:
            if dict_["test"] is False:
                logger.info(f"This movie {dict_['id']} IS NOT updated! ")

        logger.info(F"============ TEST CASE {test_case} / 1 PASSED ===========")
