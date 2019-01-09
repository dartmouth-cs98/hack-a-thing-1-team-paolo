import datetime
import time
import os

from urllib.request import urlretrieve

url = 'https://rotogrinders.com/projected-stats/nba-player.csv?site=draftkings'
destination = 'rotogrinders_predictions.csv'

def scrape_rotogrinders_predictions():
    urlretrieve(url, destination)
