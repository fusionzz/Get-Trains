import gtfs_realtime_pb2
import requests
from google.protobuf.json_format import MessageToDict

def get_feed(url):

    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(url)
    feed.ParseFromString(response.content)
    # f = open("train_info.txt", "w")
    # f.write(str(feed))
    # f.close()
    return feed
