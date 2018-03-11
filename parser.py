import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_file")
parser.add_argument("output_file")
args = parser.parse_args()

data_file = open(args.data_file)
(header,data) = data_file.read().split("__")

points = []
for datum in data.split("\n"):
    if datum is '':
        continue

    sp = datum.split("_")
    points.append({
        "count": sp[0],
        "stocks1": sp[2],
        "stocks2": sp[6],
        "percent1": sp[1],
        "percent2": sp[5] 
    })

with open(args.output_file, "w") as output_file:
    fieldnames = points[0].keys()

    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    for point in points:
        writer.writerow(point)

data_file.close()