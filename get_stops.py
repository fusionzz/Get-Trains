import csv


def get_train_stops(train):

    filename = "google_transit/stops.txt"
    fields = []
    stops = []

    with open(filename, "r") as file:
        filereader = csv.reader(file)

        fields = next(filereader)

        for row in filereader:
            if row[0][0] == train:
                stops.append(row)
    return stops