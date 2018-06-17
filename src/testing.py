import json
from khinsider import *

def test_json_output(links):
	return json.loads(get_track_info(links))


if __name__ == '__main__':
	output = test_json_output('https://downloads.khinsider.com/game-soundtracks/album/falskaar-original-soundtrack')
	print(output['total_tracks'])