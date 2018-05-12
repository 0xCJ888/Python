import json

def printMatchData(data, member):
        count = 0
        for d in data:
            count += 1
            if(count < 4):
                continue
            else:  
                print(d + ': ' + member[d] +'\t', end = '')
        print()
                

fpif = open('AQI.json', 'r', encoding="utf-8")
record = json.load(fpif)
fpif.close()

while(1):
    data = input('>')
    data = data.split()
    print(data)
    if(data[0] == 'exit' or data[0] == 'quit'):
        break
    elif(data[0] == 'match'):
        for member in record:
            if(data[1] == 'SiteName' or data[1] == 'County'):
                if(member[data[1]] == data[2]):
                    printMatchData(data, member)
            else:
                if(int(member[data[1]]) < int(data[2])):
                    printMatchData(data, member)
    elif(data[0] == 'less'):
        for member in record:
            if(data[1] == 'SiteName' or data[1] == 'County'):
                if(member[data[1]] == data[2]):
                    printMatchData(data, member)
            else:
                if(int(member[data[1]]) < int(data[2])):
                    printMatchData(data, member)
    elif(data[0] == 'greater'):
        for member in record:
            if(data[1] == 'SiteName' or data[1] == 'County'):
                if(member[data[1]] == data[2]):
                    printMatchData(data, member)
            else:
                if(int(member[data[1]]) > int(data[2])):
                    printMatchData(data, member)
