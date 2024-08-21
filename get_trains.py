import gtfs_realtime_pb2
import requests
from google.protobuf.json_format import MessageToDict

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l')
feed.ParseFromString(response.content)
f = open("train_info.txt", "w")
f.write(str(feed))
f.close()