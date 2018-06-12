import csv


def clean(row):
    for i in range(3):
        row[i] = row[i].strip()
        if row[i] == 'VALUE!' or row[i] == '' or len(row[i]) < 10:
            return False
    return row


input_file = csv.reader(open('data/chat-data-01.csv','r', encoding="utf8", errors='ignore'))
test_question = open('data/test-question.txt','a')
test_response = open('data/test-response.txt','a')
training_question = open('data/training-question.txt','a')
training_response = open('data/training-response.txt','a')


for row in input_file:
    row = clean(row)
    if row:
        print(row)
        test_question.write(row[1] + '\n')
        test_response.write(row[2] + '\n')
        training_question.write(row[1] + '\n')
        training_response.write(row[2] + '\n')
