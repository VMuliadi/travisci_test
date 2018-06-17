# -*- coding: utf-8 -*-

import re
import json
import pytest
from vgmdb import get_vgmdb


def test_case_scenario_vgmdb():
	json_response = json.loads(get_vgmdb('https://vgmdb.net/album/11939'))
	assert bool(re.search(r'\d{1}:\d{1}', json_response['total_length'])) == True
	assert json_response['release_year'].__class__ == int \
		and bool(re.search(r'\d{4}', str(json_response['release_year']))) == True
