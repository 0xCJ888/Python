import getopt
import sys

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC']

csv_file = "daily_power_supply.csv"
batchProcess = "batch-eg_csv_table_filter-sales.txt"
headerList = []
groupList = []
unitList = []
groupPrint = []
unitPrint = []
pieList = []


def inputStr(s):
    global csv_file
    global unitList
    global unitPrint
    isSaved = False

    if s[0] == "exit" or s[0] == "quit":
        sys.exit()
    elif s[0] == "index":
         print("Index\tData Name")
         for i in range(len(headerList)):
             print(i, "\t", headerList[i], sep = "")
    elif s[0] == "name": 
        print("Data Name")
        for i in range(len(headerList)):
            print(headerList[i])
    elif s[0] == "find":
        print(df[s[1:]].to_csv(sep='\t', index=False))
    elif s[0] == "help":
        if len(s) == 1:
            print("you can use help XXX to see more details....")
        elif len(s) == 2:
            helpUsage(s[1])
    elif s[0] == "save":
        isSaved = True
        saveFileName = s[1]
    if len(s) > 2:
        if s[0] == "list" or s[2] == "list":
            if isSaved:
                pltDf = convert2List(s[3:])
                saveFile = open(saveFileName, 'w')
                saveFile.write(pltDf.to_csv(sep='\t', index=False))
                saveFile.close()
            else:
                pltDf = convert2List(s[1:])
                print(pltDf.to_csv(sep='\t', index=False))
            isSaved = False
        if s[0] == "chart" or s[2] == "chart":
            if isSaved:
                shiftIndex = 2
            else:
                shiftIndex = 0

            if csv_file == "eg_csv_table_filter-sales.csv":
                strDate = "Date"
            elif csv_file == "daily_power_supply.csv":
                strDate = "日期"

            title = s[2+shiftIndex]

            if s[1+shiftIndex] == "pie":
                pieList, pltDf = convert2targetList(s, shiftIndex)
            else:
                xlabel = s[3+shiftIndex]
                ylabel = s[4+shiftIndex]
                pltDf = convert2List(s[5+shiftIndex:])

            if s[1+shiftIndex] == "line":
                ax = pltDf.plot(x = strDate, linewidth = 4)
                if csv_file == "eg_csv_table_filter-sales.csv":
                    ax.set_xlim(pltDf.Date.values[0], pltDf.Date.values[-1])
                elif csv_file == "daily_power_supply.csv":
                    ax.set_xlim(pltDf.日期.values[0], pltDf.日期.values[-1])
            elif s[1+shiftIndex] == "stack":
                ax = pltDf.plot.area(x = strDate)
                if csv_file == "eg_csv_table_filter-sales.csv":
                    ax.set_xlim(pltDf.Date.values[0], pltDf.Date.values[-1])
                elif csv_file == "daily_power_supply.csv":
                    ax.set_xlim(pltDf.日期.values[0], pltDf.日期.values[-1])
            elif  s[1+shiftIndex] == "bar":
                ax = pltDf[pltDf.columns.values.tolist()].plot.bar(x = strDate, fontsize = 20)
                if csv_file == "eg_csv_table_filter-sales.csv":
                    ax.set_xticklabels(pltDf.Date.values, rotation=0)
                elif csv_file == "daily_power_supply.csv":
                    ax.set_xticklabels(pltDf.日期.values, rotation=0)
            elif  s[1+shiftIndex] == "pie":
                plt.pie(pieList, labels=pltDf.columns.values, autopct='%1.1f%%')

            if s[1+shiftIndex] != "pie":
                plt.title(title, fontsize=30)
                plt.xlabel(xlabel, fontsize=25)
                plt.ylabel(ylabel, fontsize=25)
                plt.legend(loc = 'upper center', ncol = 3)
            else:
                targetDate = s[3+shiftIndex]
                title = targetDate + title
                plt.title(title, fontsize=30)
            if isSaved:
                plt.savefig(saveFileName, bbox_inches='tight')
            else:
                plt.show()
            isSaved = False
            plt.close()

def determineList(stri):
    global groupList
    global unitList
    isGroup = False
    isUnit = False
    for sList in stri:
        if sList == "group":
            isGroup = True
            isUnit = False
            continue
        elif sList == "unit":
            isUnit = True
            isGroup = False
            continue
        else:
            if isGroup:
                groupList.append(sList)
            elif isUnit:
                unitList.append(int(sList))
            
def determineUnit(dlist):
    global unitPrint
    global headerList
    for dVal in dlist:
        val = int(dVal)
        for headerIndex in range(len(headerList)):
            if val == headerIndex:
                unitPrint.append(headerList[headerIndex])

def determineGroup():
    global groupList
    global groupPrint
    global headerList
    tmpHeader = groupList[0]
    groupList.pop(0)
    tmpIndex = -1
    for hData in headerList:
        for gData in groupList:
            tmpIndex = headerList.index(hData)
            if gData.isdigit():
                intGData = int(gData)
            else:
                break
            if tmpIndex == intGData:
                groupPrint.append(hData)
                groupList.remove(gData)

def determineDateIndex(startDate, endDate):
    global csv_file
    tmpIndex = 0
    startIndex = 0
    endIndex = 0
    if csv_file == "eg_csv_table_filter-sales.csv":
        strDate = "Date"
    elif csv_file == "daily_power_supply.csv":
        strDate = "日期"

    for date in df[strDate]:
        if date == startDate:
            startIndex = tmpIndex
        elif date == endDate:
            endIndex = tmpIndex+1
        tmpIndex += 1

    if startDate == endDate:
        endIndex = startIndex + 1
    return startIndex, endIndex

def determineTargetDate(targetDate):
    tmpIndex = 0
    targetIndex = 0
    if csv_file == "eg_csv_table_filter-sales.csv":
        strDate = "Date"
    elif csv_file == "daily_power_supply.csv":
        strDate = "日期"
        
    for date in df[strDate]:
        if date == int(targetDate):
            targetIndex = tmpIndex
            return targetIndex
        tmpIndex += 1

def clearList():
    groupList.clear()
    unitList.clear()
    groupPrint.clear()
    unitPrint.clear()

def convert2List(listData):
    global unitList
    global groupList
    startDate = int(listData[0])
    endDate = int(listData[1])
    determineList(listData[2:])
    determineUnit(unitList)
    startIndex, endIndex = determineDateIndex(startDate, endDate)
    numberGroup = 1
    if len(groupList) == 0:
        pltDf = df.iloc[startIndex:endIndex, [0]+unitList]
    while len(groupList) != 0:
        groupName = groupList[0]
        determineGroup()
        df[groupName] = df.loc[startIndex:endIndex, groupPrint].sum(axis=1)
        numberGroup += 1
        groupPrint.clear()
    numberGroupList = list(range(-1, -numberGroup, -1))
    pltDf = df.iloc[startIndex:endIndex, [0]+numberGroupList+unitList]
    return pltDf

def convert2targetList(targetListData, shiftIndex):
    global unitList
    targetDate = targetListData[3+shiftIndex]
    targetIndex = determineTargetDate(targetDate)
    determineList(targetListData[4+shiftIndex:])
    determineUnit(unitList)
    numberGroup = 1
    while len(groupList)!=0:
        groupName = groupList[0]
        determineGroup()
        df[groupName] = df.loc[targetIndex:targetIndex, groupPrint].sum(axis=1)
        numberGroup += 1
        groupPrint.clear()
    numberGroupList = list(range(-1, -numberGroup, -1))
    pltDf = df.iloc[targetIndex:targetIndex+1, numberGroupList+unitList]
    for i in pltDf.values:
        pieList = i
    return pieList, pltDf

def helpUsage(cli):
    if cli == "save":
        print("command : save fileName chart ... or line...")
    elif cli == "index":
        print("output to terminal with all data and index")
    elif cli == "name":
        print("output to terminal with all data")
    elif cli == "list":
        print("filter data")
        print("command : list startDate endDate data")
    elif cli == "find":
        print("command : find dataName1 dataName2")
    elif cli == "chart":
        print("chart data")
        print("you can plot four kinds of pictures")
        print("plotKinds : line, stack, bar expect pie")
        print("command : chart plotKinds title xlabel ylabel startDate endDate data")
        print("command for pie")
        print("command : chart pie title targetDate data")
    else:
        print("No command for ", cli)
if "__main__" == __name__:
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:b:")
    except:
        print("Usage: %s [-d|-b] args...", sys.argv[0])
        sys.exit(2)
    if len(opts)!=0:
        for opt, arg in opts:
            if opt == "-d":
                csv_file = arg
                df = pd.read_csv(csv_file, header=0)
                headerList = df.columns.values.tolist()
            elif opt == "-b":
                batchProcess = arg
                batchFile = open(batchProcess, 'r', encoding = 'utf8')
                filetext = batchFile.read().split(';')
                for line in filetext:
                    if len(line) != 1:
                        df = pd.read_csv(csv_file, header=0)
                        headerList = df.columns.values.tolist()
                        tmpStream = line.split()
                        inputStr(tmpStream)
                        clearList()
                batchFile.close()
            else:
                assert False, "unhandled option"
    else:
        df = pd.read_csv(csv_file, header=0)
        headerList = df.columns.values.tolist()
        print(headerList)
        while(1):
            s = input('> ').split()
            inputStr(s)
            clearList()
