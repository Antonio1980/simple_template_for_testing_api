import allure
import pytest
from base.logger import automation_logger, logger

test_case = "TestMostPopularMovies"


@allure.testcase(test_case)
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    Functional Tests.
    1. Check that for every movie returned correct data type.
    """)
@pytest.mark.api
class TestDataTypeForEachMovie(object):

    @automation_logger(logger)
    def test_data_type_for_each_movie(self, api_client, fifty_most_popular_movies):
        allure.step("Verify that for each movie returned correct data type.")

        for item in fifty_most_popular_movies:
            res = api_client.get_movie_by_id(str(item["id"]))[0]
            assert res["original_title"] == item["original_title"]
            assert res["adult"] == item["adult"]
            assert res["backdrop_path"] == item["backdrop_path"]

        logger.info(F"============ TEST CASE {test_case} / 3 PASSED ===========")