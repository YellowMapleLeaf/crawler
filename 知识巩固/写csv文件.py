import csv


def writeCsv(path,data):

    with open(path,'w') as file:
        writer=csv.writer(file)
        for line in data:
            writer.writerow(line)



path="csvFile.csv"
writeCsv(path,[[1,2,3],[4,5,6]])

