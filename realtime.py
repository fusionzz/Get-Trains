import get_stops
import get_trains
import os
import time

stops = {}
temp_stops = get_stops.get_stops_no_direction()
for stop in temp_stops:
    stops[stop[0]] = 0

os.system("cls")

urls = {
        "ACE":'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace', 
        "G":'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g',
        "NQRW": 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
        "1234567": 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
        "BDFM": 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
        "JZ": 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz',
        "L": 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l'
        }

while True:
    start = time.time()
    for trains in urls.keys():
        url = urls[trains]
        feed = get_trains.get_feed(url)
        for train in feed.entity:
            stop = train.vehicle.stop_id
            status = train.vehicle.current_status
            if not stop:
                continue
            stop = stop[:-1]
            #STOPPED_AT is enum 1
            if status == 1:
                stops[stop] = "X"
            # elif train.vehicle.current_status == 2:
            #     trains[pos] = "W"
            else:
                stops[stop] = 0

    print(stops)
    end = time.time()
    print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
    time.sleep(1)
    os.system("cls")

