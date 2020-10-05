import json
from json import JSONDecodeError

import requests

from config_definitions import BaseConfig
from base.constants import RESPONSE_TEXT
from base.logger import logger, automation_logger


class ApiClient:
    api_url = BaseConfig.BASE_URL
    headers = {'Content-Type': "application/json", 'Authorization': BaseConfig.TOKEN_V4,
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    @automation_logger(logger)
    def get_most_popular_movies(self):
        uri = self.api_url + "movie/popular"
        querystring = {"api_key": BaseConfig.TOKEN_V3, "language": "en-US", "page": 1}
        try:
            _response = requests.get(url=uri, params=querystring)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.error(F"{e.__class__.__name__} create_api_token failed with error: {e}")
            raise e