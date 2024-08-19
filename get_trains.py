import nyct_subway_pb2
import requests

feed = nyct_subway_pb2.gtfs__realtime__pb2.FeedMessage()
response = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l')
feed.ParseFromString(response.content)
f = open("train_info.txt", "w")
for entity in feed.entity:
  f.write(str(entity))
  print(entity.id)

f.close()