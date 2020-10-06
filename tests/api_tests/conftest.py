import pytest
from base.logger import automation_logger, logger


@pytest.fixture(scope="session")
@automation_logger(logger)
def fifty_most_popular_movies(api_client):
    _response1 = api_client.get_most_popular_movies()[0]["results"]
    _response2 = api_client.get_most_popular_movies(page=2)[0]["results"]
    _response3 = api_client.get_most_popular_movies(page=3)[0]["results"][:10]

    return _response1 + _response2 + _response3
