import sys, getopt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 50})
csv_file = "eg_csv_table_filter-sales.csv"
headerList = []
groupList = []
unitList = []
groupPrint = []
unitPrint = []

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
            pass
        else:
            assert False, "unhandled option"

def inputStr():
    global csv_file
    global unitList
    global unitPrint
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
    elif s[0] == "list":
        pltDf = convert2List(s[1:])
        print(pltDf.to_csv(sep='\t', index=False))
    elif s[0] == "chart":
        title = s[2]
        if s[1] == "pie":
            targetDate = s[3]
            determineList(s[4:])
            determineUnit(unitList)
            determineGroup()
            print("groupList", groupList)
            print("unitList", unitList)
            print("unitPrint", unitPrint)
            print("groupPrint", groupPrint)
            if len(groupList) != 0:
                df[groupList[0]] = df.loc[:, groupPrint].sum(axis=1)
                pltDf = df.iloc[:, [0]+[-1]+unitList]
            else:
                pass
        else:
            xlabel = s[3]
            ylabel = s[4]
            pltDf = convert2List(s[5:])
        if s[1] == "line":
            ax = pltDf.plot(x = 'Date', linewidth = 4)
            ax.set_xlim(pltDf.Date.values[0], pltDf.Date.values[-1])
        elif s[1] == "stack":
            ax = pltDf.plot.area(x = 'Date')
            ax.set_xlim(pltDf.Date.values[0], pltDf.Date.values[-1])
        elif  s[1] == "bar":
            ax = pltDf[pltDf.columns.values.tolist()].plot.bar(x = 'Date', fontsize = 20)
            ax.set_xticklabels(pltDf.Date.values, rotation=0)
        elif  s[1] == "pie":
            pltDf.plot.pie()
        if s[1] != "pie":
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.legend(loc = 'upper center', ncol = 3)
        
        plt.show()

    elif s[0] == "save":
        pass

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
    for hData in headerList:
        for gData in groupList[1:]:
            if hData.find(groupList[0]) == 0:
                if hData.find(gData):
                    groupPrint.append(hData)
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

def clearList():
    groupList.clear()
    unitList.clear()
    groupPrint.clear()
    unitPrint.clear()

def convert2List(listData):
    global unitList
    startDate = int(listData[0])
    endDate = int(listData[1])
    determineList(listData[2:])
    determineUnit(unitList)
    startIndex, endIndex = determineDateIndex(startDate, endDate)
    determineGroup()
    df[groupList[0]] = df.loc[startIndex:endIndex, groupPrint].sum(axis=1)
    pltDf = df.iloc[startIndex:endIndex, [0]+[-1]+unitList]
    return pltDf


if "__main__" == __name__:
    main()
    df = pd.read_csv(csv_file, header=0)
    headerList = df.columns.values.tolist()
    while(1):
        inputStr()
        print("groupList", groupList)
        print("unitList", unitList)
        print("unitPrint", unitPrint)
        print("groupPrint", groupPrint)
        clearList()

