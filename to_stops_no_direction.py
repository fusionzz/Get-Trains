import csv

with open("google_transit/stops.txt", "r") as file:
    with open("stops_no_direction.csv", "w") as new_file:
        filereader = csv.reader(file)

        filewriter = csv.writer(new_file)

        headers = next(filereader)

        filewriter.writerow(headers)

        for row in filereader:
            if row[0][-1] != "N" and row[0][-1] != "S":
                filewriter.writerow(row)

