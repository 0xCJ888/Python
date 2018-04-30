import random

count = 0
job = 0
coreList = []
queue = []
core = 0
tempCore = 0
isCoreEmpty = []
flagAdd = False
flag_getjob = True
flag_progress = False

def job_gen():
    return random.random() < 0.18

def priority_gen():
    return random.randint(0, 7)

def workTime_gen():
    return random.randint(1, 100)

def printJobList(pList):
    testfile.write( '\t\tjob: ' + str(pList.getJob()) + 
                    ' wait ' + str(pList.getWait()) + ' ,' 
                    ' priority ' +str(pList.getPriority()) + ' , ' +
                    str(pList.getWorkTime()) + ' cycles.\n')

def printCoreList(pList):
    testfile.write('\tcore ' + str(tempCore) + 
                    ' run job ' + str(pList.getJob()) + 
                    ' of priority ' + str(pList.getPriority()) + 
                    ' (waiting ' +str(pList.getWait()) + ' times) ' + 
                    'use ' + str(pList.getWorkTime()) + ' cycles.\n')

class Core():
    def __init__(self, job, priority, worktime, wait):
        self.job = job
        self.priority = priority
        self.worktime = worktime
        self.wait = wait
    def __repr__(self):
        return repr((self.job, self.priority, self.worktime))
    def getJob(self):
        return self.job
    def getPriority(self):
        return self.priority
    def getWorkTime(self):
        return self.worktime
    def getWait(self):
        return self.wait
    def working(self, wstate):
        next_state = wstate
        if wstate == flag_progress:
            self.worktime -= 1
            if self.worktime > 0:
                next_state = flag_progress
            else:
                next_state = flag_getjob
        return next_state
    def clear(self):
        self.job = 0
        self.priority = 0
        self.worktime = 0
    def waitCount(self):
        self.wait +=1 

c = Core(0, 0, 0, 0)
testfile = open('hw07_log_jobs.txt', 'w')
testfile.write('Run Job Log \nHistory\n')
while(count < 3600):
    testfile.write('Time ' + str(count) + ': ')
    if(job_gen()):  
        job += 1
        priority = priority_gen()
        workTime = workTime_gen()
        c = Core(job, priority, workTime, 0)
        # core finish, wait to add
        for i in range(0, len(isCoreEmpty)):
            if(isCoreEmpty[i]):
                isCoreEmpty[i] = False
                coreList[i] = c
                tempCore = i
                flagAdd = True
                break
        # most 10 core
        if(core < 10):
            testfile.write('1 jobs in queue.\n\tQueue information:\n')
            if(not flagAdd):
                isCoreEmpty.append(False)
                coreList.append(c)
                tempCore = core
                core += 1
            flagAdd = False
            printJobList(coreList[tempCore])
            printCoreList(coreList[tempCore])
        else:
            if(not flagAdd):
                queue.append(c)
            elif(len(queue) == 0):
                testfile.write(('1 jobs in queue.\n'))
                flagAdd = False
                printCoreList(coreList[tempCore])

    elif(len(queue) == 0):
        testfile.write('0 jobs in queue.\n')

    if(core >= 10 and len(queue) != 0):
        for i in range(0, len(isCoreEmpty)):
            if(isCoreEmpty[i]):
                isCoreEmpty[i] = False
                tempCore = i
                flagAdd = True
                break

        testfile.write(str(len(queue)) + ' jobs in queue.\n')
        # print queue
        for i in range(0,len(queue)):
            printJobList(queue[i])
        if(flagAdd):
            flagAdd = False
            flagWaitOver = False
            # wait over 10 times
            for i in range(0, len(queue)):
                if(queue[i].getWait() > 10):
                    index = i
                    flagWaitOver = True
                    break
            if(not flagWaitOver):
                flagWaitOver = False
                m = max(queue, key=lambda core: core.priority)
                tmp = []
                tmpcount = 0
                for i in range(0, len(queue)):
                    if(queue[i].getPriority() == m.getPriority()):
                        tmp.append(queue[i])
                        tmpcount += 1
                if(tmpcount > 1):
                    m = min(queue, key=lambda core: core.worktime)
                index = queue.index(m)

            coreList[tempCore] = queue.pop(index)
            printCoreList(coreList[tempCore])
            for i in range(0,len(queue)):
                queue[i].waitCount()
    # working
    for i in range(0,len(coreList)):
        isCoreEmpty[i] = coreList[i].working(flag_progress)
        if(isCoreEmpty[i]):
            coreList[i].clear()
            break
    count += 1

testfile.write('Total ' + str(job) +' jobs.\n')
testfile.write('\tExecuted ' + str(job - len(queue)) +' jobs.\n')
if(len(queue) != 0):
    testfile.write('\tStill on waiting ' + str(len(queue)))
    testfile.write('\nOn waiting list:\n')
    for i in range(len(queue)):
        printJobList(queue[i])
testfile.close()