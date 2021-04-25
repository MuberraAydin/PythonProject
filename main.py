from datetime import datetime
import json
import random
import os

def get_timestamp(string: str):
    return int(datetime.strptime(string,"%Y-%m-%d %H:%M:%S").timestamp())


if "yellow_tripdata_2020-12.csv" not in os.listdir():
    print("yellow_tripdata_2020-12.csv not found in the directory.")
    exit()


print("Reading file...")


with open("yellow_tripdata_2020-12.csv","r") as f:
    header = f.readline().strip().split(",")
    lines = [line.strip().split(",") for line in f.readlines()]


print("File read. Shuffling lines...")

random.shuffle(lines)

row_count = int(input("Number of records to be included from each day of the month: "))

data_by_day = {}

for i in range(1,32):
    data_by_day.update({i: []})

for sl in lines:
    if "" in sl:
        continue

    el ={
        header[0]: sl[0],
        header[1]: get_timestamp(sl[1]),
        header[2]: get_timestamp(sl[2]),
        header[3]: int(sl[3]),
        header[4]: float(sl[4]),
        header[5]: sl[5],
        header[6]: sl[6],
        header[7]: sl[7],
        header[8]: sl[8],
        header[9]: sl[9],
        header[10]: sl[10],
        header[11]: sl[11],
        header[12]: sl[12],
        header[13]: sl[13],
        header[14]: sl[14],
        header[15]: sl[15],
        header[16]: float(sl[16]),
        header[17]: sl[17]
    }
    day = datetime.fromtimestamp(el[header[1]]).day
    data_by_day[day].append(el)


final_data = []


for i in range(1,32):
    final_data += data_by_day[i][:row_count]


locations = []

for el in final_data:
    if el["PULocationID"] not in locations:
        locations.append(el["PULocationID"])


print("Data is ready. Records from "+ str(len(locations)) + " different locations has been saved. Writing into files...")


with open("data.json","w",encoding="utf-8") as f:
    json.dump(final_data, f, indent = 4)


with open("data.csv","w",encoding="utf-8") as f:
    f.write(",".join(header) + "\n")
    for row in final_data:
        f.write(",".join([str(row[col]) for col in row]) + "\n")


print("Files saved!")




