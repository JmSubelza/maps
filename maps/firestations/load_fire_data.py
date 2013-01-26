import sys 
import os 

sys.path.append('/Users/duanehilton/sites/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps/firestations')
os.environ['DJANGO_SETTINGS_MODULE'] = 'maps.maps.settings'

import json
import urllib2
from firestations.models import Station 
#from urlgrabber import urlread


class ChiData:

    def __init__(self, url='http://data.cityofchicago.org/api/views/28km-gtjn/rows.json'):
        self.data = json.load(urllib2.urlopen(url))
    
    def load(self):
        for x in range(len(self.data['data'])):
            lt=self.data['data'][x][14][1] 
            lg=self.data['data'][x][14][2] 
            if lt and lg:
                inst = Station(address=self.data['data'][x][9], 
                               lat=lt, 
                               lng=lg) 
                inst.save()


def main():
    dat = ChiData()
    dat.load()


if __name__ == '__main__':
    main()
