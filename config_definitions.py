import os
import configparser


def get_parser(config):
    parser = configparser.ConfigParser()
    with open(config, mode='r', buffering=-1, closefd=True):
        parser.read(config)
        return parser


class BaseConfig:

    config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')
    parser = get_parser(config_file)

    BASE_URL = parser.get("URL's", 'base_url')

    TOKEN = parser.get("ARG's", 'token')
    TOKEN_V3 = parser.get("ARG's", 'token_v3')
    TOKEN_V4 = parser.get("ARG's", 'token_v4')
