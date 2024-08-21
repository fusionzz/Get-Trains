from get_stops import get_train_stops
import os
import time

stops = [stop[0] for stop in get_train_stops("L")]
trains = [0 for i in range(len(stops))]

os.system("cls")

pos = 0

while True:
    trains[pos] = 0
    pos = (pos + 1) % len(stops)
    trains[pos] = "X"
    print(stops)
    print(trains)
    time.sleep(1)
    os.system("cls")
