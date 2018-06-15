# -*- coding: utf-8 -*-

import json
import pytest
import re
from vgmdb import get_vgmdb
# print(get_vgmdb('https://vgmdb.net/album/11939'))

def test_json_output():
	json_response = json.loads(get_vgmdb('https://vgmdb.net/album/11939'))
	assert bool(re.search(r'\d{2}:\d{2}', json_response['total_length'])) == True
	assert json_response['release_year'].__class__ == int \
		and bool(re.search(r'\d{4}', str(json_response['release_year']))) == True