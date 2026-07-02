import csv
import os


csv_path = os.path.join(os.path.dirname(__file__), 'Asset', 'LOCAL_PEOPLE_DONG_201912_1weeks.csv')


age = ['10대','20대','30대','40대','50대','60대','70대이상']
group_ids= [[0,1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13]]
year = [0] * len(age)
with open(csv_path,'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    data = list(reader)

    for raw in data:
        for i in range(len(age)):
            idx = group_ids[i]
            total=0;
            for j in idx:
                total += float(raw[j+4]) + float(raw[j+18])
            year[i] += total


    for i in range(len(age)):
        avg = year[i]/len(data)
        print(f"{age[i]} : {avg}")

