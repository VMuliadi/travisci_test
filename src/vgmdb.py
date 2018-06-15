# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

def get_vgmdb(vgmdb_url):
    album_information = {}
    vgmdb_request = requests.get(vgmdb_url)
    scraping_request = BeautifulSoup(vgmdb_request.text, 'html.parser')
    general_info = scraping_request.findAll('table', {'id':'album_infobit_large'})[0]
    album_information['catalog_number'] = general_info.findAll('tr')[0].findAll('td')[1].get_text().split()[0]
    try:
        album_information['release_year'] = int(general_info.findAll('tr')[1].findAll('td')[1]\
            .get_text().split(',')[1].split()[0])
        album_information['publish_format'] = general_info.findAll('tr')[2].findAll('td')[1].get_text()
        album_information['release_price'] = general_info.findAll('tr')[3].findAll('td')[1].get_text()
        album_information['media_format'] = general_info.findAll('tr')[4].findAll('td')[1].get_text()
        album_information['classification'] = general_info.findAll('tr')[5].findAll('td')[1].get_text()
        album_information['published_by'] = general_info.findAll('tr')[6].findAll('td')[1].get_text()
        album_information['composer'] = general_info.findAll('tr')[7].findAll('td')[1].get_text()
        album_information['arranged_by'] = general_info.findAll('tr')[8].findAll('td')[1].get_text()
        album_information['performed_by'] = general_info.findAll('tr')[9].findAll('td')[1].get_text()
    except IndexError:
        album_information['release_year'] = int(general_info.findAll('tr')[4].findAll('td')[1]\
            .get_text().split(',')[1].split()[0])
        album_information['publish_format'] = general_info.findAll('tr')[5].findAll('td')[1].get_text()
        album_information['release_price'] = general_info.findAll('tr')[6].findAll('td')[1].get_text()
        album_information['media_format'] = general_info.findAll('tr')[7].findAll('td')[1].get_text()
        album_information['classification'] = general_info.findAll('tr')[8].findAll('td')[1].get_text()
        album_information['published_by'] = general_info.findAll('tr')[9].findAll('td')[1].get_text()
        album_information['composer'] = general_info.findAll('tr')[10].findAll('td')[1].get_text()
        album_information['arranged_by'] = general_info.findAll('tr')[11].findAll('td')[1].get_text()
        album_information['performed_by'] = general_info.findAll('tr')[12].findAll('td')[1].get_text()

    album_information['track_info'] = []
    for tracklist in scraping_request.findAll('div', {'id':'tracklist'})[0]\
        .findAll('span',{'class':'tl'})[0].findAll('table', {'cellpadding':'1'})[0].findAll('tr'):
            track_information = {}
            track_information['track_number'] = tracklist.findAll('td')[0].get_text()
            track_information['track_title'] = tracklist.findAll('td')[1].get_text()
            track_information['track_length'] = tracklist.findAll('td')[-1]\
                .findAll('span', {'class':'time'})[0].get_text()
            album_information['track_info'].append(track_information)
    album_information['total_length'] = scraping_request.findAll('div', {'id':'tracklist'})[0]\
        .findAll('span', {'class':'tl'})[0].findAll('span')[-1].get_text()

    return json.dumps(album_information)
