import re
import json
import pytest
from khinsider import *

def test_case_scenario_khinsider():
	json_response = json.loads(get_track_info('https://downloads.khinsider.com/game-soundtracks/album/falskaar-original-soundtrack'))
	for trackinfo in json_response['tracklist_info']:
		assert bool(re.search(r'\w', trackinfo['track_title'])) == True
		assert bool(re.search(r'\d{1}:\d{1}', trackinfo['track_length'])) == True
		assert json_response['total_tracks'].__class__ == int and \
			bool(re.search(r'\d', str(json_response['total_tracks']))) == True
