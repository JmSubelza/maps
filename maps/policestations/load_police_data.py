import sys 
import os 

sys.path.append('/Users/duanehilton/sites/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps/policestations')
os.environ['DJANGO_SETTINGS_MODULE'] = 'maps.maps.settings'

import json
import urllib2
from policestations.models import Station 
#from urlgrabber import urlread


class ChiData:

    def __init__(self, url='http://data.cityofchicago.org/api/views/z8bn-74gv/rows.json'):
        self.data = json.load(urllib2.urlopen(url))
       # self.un = un
       # self.pw = pw 
       # self.geo = []

#    def _geocode(self):
#        for x in range(len(self.data['data'])):
#            address =  self.data['data'][x][1].replace(' ', '+') + ',+Chicago+IL'
#            url = 'http://%s:%s@geocoder.us/member/service/csv/geocode?address=%s' % (self.un, self.pw, address)
#            line = urlread(url.encode('ascii'))
#            fields = line.split(',')
#            self.geo.append(fields)
            #lat, lng, address, city, state, zip
    
    def load(self):
       # if self.geo == []:
       #     self._goecode()
        for x in range(len(self.data['data'])):
            lt=self.data['data'][x][17][1] 
            lg=self.data['data'][x][17][2] 
            if lt and lg:
                inst = Station(address=self.data['data'][x][9], 
                               url=self.data['data'][x][13][0], 
                               phone=self.data['data'][x][14][0], 
                               lat=lt, 
                               lng=lg) 
                inst.save()


def main():
    dat = ChiData()
    dat.load()


if __name__ == '__main__':
    main()
