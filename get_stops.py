import csv

filename = "google_transit/stops.txt"
fields = []
stops = []

train = "L"

with open(filename, "r") as file:
    filereader = csv.reader(file)

    fields = next(filereader)

    for row in filereader:
        if row[0][0] == "L":
            stops.append(row)


print(fields)
print(stops)