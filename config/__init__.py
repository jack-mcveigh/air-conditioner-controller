import os
import json

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

with open(f'{BASEDIR}/config/config.json', 'r') as config_fp:
    _config = json.load(config_fp)

SL_USERNAME = _config['smart_life']['username']
SL_PASSWORD = _config['smart_life']['password']
SL_COUNTRYCODE = _config['smart_life']['country_code']
SL_APPLICATION = _config['smart_life']['application']
