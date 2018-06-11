import csv


def clean(row):
    row[0] = row[0].strip()
    row[1] = row[1].strip()
    row[2] = row[2].strip()
    return row


with open('data/chat-data-01.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        row = clean(row)
        print(row)
