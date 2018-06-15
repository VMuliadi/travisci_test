# -*- coding: utf-8 -*-

import json
import pytest
from vgmdb import get_vgmdb
# print(get_vgmdb('https://vgmdb.net/album/11939'))

def test_json_output():
	json_response = json.loads(get_vgmdb('https://vgmdb.net/album/11939'))
	assert 2009 == json_response['release_year']
	assert 0 < len(json_response['track_info'])
	assert 'DERD-10001' == json_response['catalog_number']
