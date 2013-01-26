import sys 
import os 

sys.path.append('/Users/duanehilton/sites/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps/libraries')
os.environ['DJANGO_SETTINGS_MODULE'] = 'maps.maps.settings'

import json
import urllib2
from libraries.models import Library 


class ChiData:

    def __init__(self, url='http://data.cityofchicago.org/api/views/x8fc-8rcq/rows.json'):
        self.data = json.load(urllib2.urlopen(url))

    def load(self):
        for x in range(len(self.data['data'])):
            inst = Library(hours=self.data['data'][x][9], 
                           location=self.data['data'][x][8], 
                           address=self.data['data'][x][12], 
                           url=self.data['data'][x][17][0], 
                           phone=self.data['data'][x][16], 
                           lat=self.data['data'][x][18][1], 
                           lng=self.data['data'][x][18][2])
            inst.save()


def main():
    dat = ChiData()
    dat.load()


if __name__ == '__main__':
    main()
