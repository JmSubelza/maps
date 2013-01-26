import json
import urllib2
import sys, os 
sys.path.append('/Users/duanehilton/sites/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps')
sys.path.append('/Users/duanehilton/sites/maps/maps/libraries')
os.environ['DJANGO_SETTINGS_MODULE'] = 'maps.maps.settings'

from libraries.models import Library 

data = json.load(urllib2.urlopen('http://data.cityofchicago.org/api/views/x8fc-8rcq/rows.json'))

for x in range(len(data['data'])):
    inst = Library(address=data['data'][x][12], lat=data['data'][x][18][1], lng=data['data'][x][18][2])
    inst.save()
    #print '%s, %s, %s' % (data['data'][x][12], data['data'][x][18][1], data['data'][x][18][2])
