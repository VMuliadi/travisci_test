# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

def get_track_info(links):
	track_information = {}
	if not links.startswith('http'): links = 'https://' + links

	khinsider_request = requests.get(links)
	khinsider_scrape = BeautifulSoup(khinsider_request.text, 'html.parser')
	track_information['album_name'] = khinsider_scrape.findAll('p', {'align':'left'})[0].findAll('b')[0].get_text()
	track_information['total_tracks'] = int(khinsider_scrape.findAll('p', {'align':'left'})[0].findAll('b')[1].get_text())
	track_information['total_file_size'] = khinsider_scrape.findAll('p', {'align':'left'})[0].findAll('b')[2].get_text()

	track_information['tracklist_info'] = []
	for index, track_info in enumerate(khinsider_scrape.findAll('table', {'id':'songlist'})[0].findAll('tr')):
			track_info_dict = {}
			if index > 0:
				try:
					track_info_dict['track_title'] = track_info.findAll('td', {'class':'clickable-row'})[0].get_text()
					track_info_dict['track_length'] = track_info.findAll('td', {'class':'clickable-row'})[1].get_text()
					track_info_dict['track_size'] = track_info.findAll('td', {'class':'clickable-row'})[2].get_text()
					track_information['tracklist_info'].append(track_info_dict)
				except IndexError: pass

	track_information['total_play_length'] = khinsider_scrape.findAll('tr', {'id':'songlist_footer'})[0]\
		.findAll('th', {'align':'right'})[1].get_text().replace('m','').replace('s','').replace(' ',':')
	return json.dumps(track_information)


def get_download_link(links):
	list_of_download_link = []
	base_url = 'https://downloads.khinsider.com'
	khinsider_request = requests.get(links)
	khinsider_scrape = BeautifulSoup(khinsider_request.text, 'html.parser')
	for index, track_info in enumerate(khinsider_scrape.findAll('table', {'id':'songlist'})[0].findAll('tr')):
		if index > 0:
			try:
				list_of_download_link.append(base_url + track_info.findAll('td', {'class':'clickable-row'})[0]\
					.findAll('a')[0].get('href'))
			except IndexError: pass

	download_links = []
	for index,links in enumerate(list_of_download_link):
		download_links_details = {}
		khinsider_request = requests.get(links)
		khinsider_scrape = BeautifulSoup(khinsider_request.text, 'html.parser')
		download_links_details['track_number'] = index+1
		download_links_details['filename'] = khinsider_scrape.findAll('p', {'align':'left'})[-1].findAll('b')[-1].get_text()
		download_links_details['links'] = khinsider_scrape.findAll('a', {'style':'color: #21363f;'})[0].get('href')
		download_links.append(download_links_details)
	return json.dumps(download_links, sort_keys=True)
