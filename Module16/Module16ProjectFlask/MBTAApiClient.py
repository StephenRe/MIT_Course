import urllib.request, json
import mysqldb
from datetime import datetime

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            # complete the fields below based on the entries of your SQL table
            busDict['bus_id'] = bus['id']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['route_num'] = bus['relationships']['route']['data']['id'] 
            busDict['bearing'] = bus['attributes']['bearing']
            busDict['current_status'] = bus['attributes']['current_status']
            busDict['current_stop_sequence'] = bus['attributes']['current_stop_sequence']
            busDict['direction_id'] = bus['attributes']['direction_id']
            busDict['occupancy_status'] = bus['attributes']['occupancy_status']
            busDict['updated_at'] = datetime.strptime(bus['attributes']['updated_at'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d %H:%M:%S')
            busDict['stop_id'] = bus['relationships']['stop']['data']['id']   
            busDict['trip_id'] = bus['relationships']['trip']['data']['id']  
            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList) 

    return mbtaDictList  

print(callMBTAApi())