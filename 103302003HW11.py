import getopt
import sys

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#matplotlib.rcParams.update({'font.size': 50})
csv_file = "eg_csv_table_filter-sales.csv"
batchProcess
headerList = []
groupList = []
unitList = []
groupPrint = []
unitPrint = []
pieList = []

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:b:")
    except:
        print("Usage: %s [-d|-b] args...", sys.argv[0])
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-d":
            global csv_file
            csv_file = arg
        elif opt == "-b":
            batchProcess = arg
        else:
            assert False, "unhandled option"

def inputStr():
    global csv_file
    global unitList
    global unitPrint
    isSaved = False
    s = input('> ').split()
    if s[0] == "exit" or s == "quit":
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
        print(df[s[1:]])
    elif s[0] == "help":
        pass
    elif s[0] == "save":
        isSaved = True
        saveFileName = s[1]
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

        title = s[2+shiftIndex]

        if s[1+shiftIndex] == "pie":
            pieList, pltDf = convert2targetList(s, shiftIndex)
        else:
            xlabel = s[3+shiftIndex]
            ylabel = s[4+shiftIndex]
            pltDf = convert2List(s[5+shiftIndex:])

        if s[1+shiftIndex] == "line":
            ax = pltDf.plot(x = 'Date', linewidth = 4)
            ax.set_xlim(pltDf.Date.values[0], pltDf.Date.values[-1])
        elif s[1+shiftIndex] == "stack":
            ax = pltDf.plot.area(x = 'Date')
            ax.set_xlim(pltDf.Date.values[0], pltDf.Date.values[-1])
        elif  s[1+shiftIndex] == "bar":
            ax = pltDf[pltDf.columns.values.tolist()].plot.bar(x = 'Date', fontsize = 20)
            ax.set_xticklabels(pltDf.Date.values, rotation=0)
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
    for hData in headerList:
        for gData in groupList:
            if hData.find(tmpHeader) == 0:
                if hData.find(gData):
                    groupPrint.append(hData)
                    groupList.remove(gData)
                    break

def determineDateIndex(startDate, endDate):
    tmpIndex = 0
    startIndex = 0
    endIndex = 0
    for date in df["Date" or "日期"]:
        if date == startDate:
            startIndex = tmpIndex
        elif date == endDate:
            endIndex = tmpIndex+1
        tmpIndex += 1
    return startIndex, endIndex

def determineTargetDate(targetDate):
    tmpIndex = 0
    targetIndex = 0
    for date in df["Date" or "日期"]:
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
    groupName = groupList[0]
    determineGroup()
    df[groupName] = df.loc[startIndex:endIndex, groupPrint].sum(axis=1)
    pltDf = df.iloc[startIndex:endIndex, [0]+[-1]+unitList]
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


if "__main__" == __name__:
    main()
    df = pd.read_csv(csv_file, header=0)
    headerList = df.columns.values.tolist()
    while(1):
        inputStr()
        clearList()
