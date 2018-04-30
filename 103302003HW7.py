import random

def job_gen():
    return random.random() < 0.18

def priority_gen():
    return random.randint(0, 7)

def workTime_gen():
    return random.randint(1, 100)

flag_getjob = True
flag_progress = False

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

def printList(list):
    for i in range(0,len(list)):
        testfile.write( '\t\tjob: ' + str(list[i].getJob()) + 
                        ' wait ' + str(list[i].getWait()) + ' ,' 
                        ' priority ' +str(list[i].getPriority()) + ' , ' +
                        str(list[i].getWorkTime()) + ' cycles.\n')

count = 0
job = 0
coreList = []
queue = []
core = 0
tempCore = 0
c = Core(0, 0, 0, 0)
isCoreEmpty = []
flagAdd = False

testfile = open('testfile.txt', 'w')
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
            testfile.write('\t\tjob ' + str(coreList[tempCore].getJob()) + 
                            ': wait 0,' +
                            ' priority ' + str(coreList[tempCore].getPriority()) + ', ' +
                            str(coreList[tempCore].getWorkTime()) + 'cycles.\n')
            testfile.write('\tcore ' + str(tempCore) + 
                           ' run job ' + str(coreList[tempCore].getJob()) + 
                           ' of priority ' + str(coreList[tempCore].getPriority()) + 
                           ' (waiting 0 times) ' + 'use ' + str(coreList[tempCore].getWorkTime()) + ' cycles.\n')
        else:
            if(not flagAdd):
                queue.append(c)
            else:
                testfile.write('\t\tjob ' + str(coreList[tempCore].getJob()) + 
                            ': wait 0,' +
                            ' priority ' + str(coreList[tempCore].getPriority()) + ', ' +
                            str(coreList[tempCore].getWorkTime()) + 'cycles.\n')
    elif(len(queue) == 0):
        testfile.write('0 jobs in queue.\n')

    if(core >= 10 and len(queue) != 0):
        for i in range(0, len(isCoreEmpty)):
            if(isCoreEmpty[i]):
                isCoreEmpty[i] = False
                tempCore = i
                flagAdd = True
                break

        testfile.write('\t' + str(len(queue)) + ' jobs in queue.\n')
        printList(queue)
        if(flagAdd):
            flagAdd = False
            flagWaitOver = False
            # wait over 10 times
            for i in range(0, len(queue)):
                if(queue[i].getWait == 11):
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
            testfile.write( '\t\tcore ' + str(tempCore) + 
                            ' run job ' + str(coreList[tempCore].getJob()) + 
                            ' of priority ' + str(coreList[tempCore].getPriority()) + 
                            ' (waiting ' + str(coreList[tempCore].getWait()) + ' times) ' +
                            ' use ' + str(coreList[tempCore].getWorkTime()) + ' cycles.\n')
            for i in range(0,len(queue)):
                queue[i].waitCount()
        elif(core >= 10 and len(queue) == 0):
            testfile.write(('0 jobs in queue.\n'))
    # working
    for i in range(0,len(coreList)):
        isCoreEmpty[i] = coreList[i].working(flag_progress)
        if(isCoreEmpty[i]):
            coreList[i].clear()
            break
    count += 1

testfile.close()