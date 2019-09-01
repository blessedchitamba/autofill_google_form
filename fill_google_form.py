import csv
import requests

#line variable to store each line
url = 'https://docs.google.com/forms/d/1KB4Kk9lfwaAywfqC9rz3IYOqWGBFxxo_Mvln0nBeNPk/formResponse'
submission = {}

with open('C:\\Users\Microsoft\\Documents\\PFCC Office\\2019 stuff\\dwd_reg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count<11:
            if line_count <= 2:
                #discard the first two lines
                line_count += 1
            else:
                #print('Name is',row[1],'and number is',row[2])
                submission = {"entry.2005620554":row[1], "entry.1166974658":row[2], "entry.257044540":row[3], "entry.1419001901":row[4]}
                result = requests.post(url, submission)
                print(result)
                line_count += 1
    print('Processed',line_count,'lines.')