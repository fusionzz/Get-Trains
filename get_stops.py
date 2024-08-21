import csv


def get_all_train_stops():

    filename = "google_transit/stops.txt"
    stops = []

    with open(filename, "r") as file:
        filereader = csv.reader(file)

        for row in filereader:
            stops.append(row)
    return stops

def get_stops_no_direction():
    filename = "google_transit/stops.txt"
    stops = []

    with open(filename, "r") as file:
        filereader = csv.reader(file)

        for row in filereader:
            if row[0][-1] != "N" and row[0][-1] != "S":
                print(row[0])
                stops.append(row)
    return stops

#print(get_stops_no_direction())

