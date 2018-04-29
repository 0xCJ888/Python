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

count = 0
job = 0
coreList = []
queue = []
core = 0
tempCore = 0
c = Core(0, 0, 0, 0)
isCoreEmpty = []
flagAdd = False

while(count < 3600):
    print('Time ', count, ': ', end=" ")
    if(job_gen()):  
        job += 1
        priority = priority_gen()
        workTime = workTime_gen()
        c = Core(job, priority, workTime, 0)
        for i in range(0, len(isCoreEmpty)):
            if(isCoreEmpty[i]):
                isCoreEmpty[i] = False
                #print('I want to Add')
                #print('i = ', i)
                coreList[i] = c
                tempCore = i
                flagAdd = True
                break
        if(core < 10):
            print('1 jobs in queue.')
            print('\tQueue information:')
            if(not flagAdd):
                isCoreEmpty.append(False)
                coreList.append(c)
                tempCore = core
                core += 1
            flagAdd = False
            #print('list = ', len(coreList))
            #print('tempCore = ', tempCore)
            print(  '\t\tjob:', coreList[tempCore].getJob(), 
                    'wait 0,',
                    'priority ', coreList[tempCore].getPriority(),',',
                    coreList[tempCore].getWorkTime(), 'cycles.')
            print('\t\tcore ', tempCore, 
                  'run job', coreList[tempCore].getJob(), 
                  'of priority', coreList[tempCore].getPriority(), 
                  '(waiting 0 times)', 'use', coreList[tempCore].getWorkTime(), 'cycles.')
        else:
            if(not flagAdd):
                queue.append(c)
            else:
                print('\t\tjob:', coreList[tempCore].getJob(), 
                      'wait 0, priority ', coreList[tempCore].getPriority(), ',', 
                      coreList[tempCore].getWorkTime(), 'cycles.')
                print('\t\tcore ', tempCore, 
                      'run job', coreList[tempCore].getJob(), 
                      'of priority', coreList[tempCore].getPriority(), 
                      '(waiting 0 times)', 'use', coreList[tempCore].getWorkTime(), 'cycles.')
    elif(len(queue) == 0):
        print('0 jobs in queue.')
    if(core >= 10 and len(queue) != 0):
        for i in range(0, len(isCoreEmpty)):
            if(isCoreEmpty[i]):
                isCoreEmpty[i] = False
                #print('core full')
                #print('I want to Add')
                #print('i = ', i)
                tempCore = i
                flagAdd = True
                break
        
        print('\t', len(queue), 'jobs in queue.')
        print('\tQueue information:')
        for i in range(0,len(queue)):
            print('\t\tjob:', queue[i].getJob(), 
            'wait', queue[i].getWait(), 
            'priority ', queue[i].getPriority(), ',', 
            queue[i].getWorkTime(), 'cycles.')

        if(flagAdd):
            flagAdd = False
            flagWaitOver = False
            print()
            # wait over 10 times
            for i in range(0, len(queue)):
                if(queue[i].getWait == 11):
                    index = i
                    flagWaitOver = True
                    break
            if(not flagWaitOver):
                flagWaitOver = False
                #print('After sort')
                s = sorted(queue, key=lambda core: core.priority)
                #print(s)
                m = max(queue, key=lambda core: core.priority)
                # max more than one
                tmp = []
                count = 0
                for i in range(0, len(queue)):
                    if(queue[i].getPriority() == m.getPriority()):
                        tmp.append(queue[i])
                        count += 1
                if(count > 1):
                    m = min(queue, key=lambda core: core.worktime)
                index = queue.index(m)
                #print(index)
                #print(m)

            for i in range(0,len(queue)):
                print('\t\tjob:', queue[i].getJob(), 
                'wait ', queue[i].getWait(), 
                'priority ', queue[i].getPriority(), ',',
                queue[i].getWorkTime(), 'cycles.')
            coreList[tempCore] = queue.pop(index)
            print('\t\tcore ', tempCore, 
                  'run job', coreList[tempCore].getJob(), 
                  'of priority', coreList[tempCore].getPriority(), 
                  '(waiting ',coreList[tempCore].getWait(), 'times)', 
                  'use', coreList[tempCore].getWorkTime(), 'cycles.')
            for i in range(0,len(queue)):
                queue[i].waitCount()
    for i in range(0,len(coreList)):
        isCoreEmpty[i] = coreList[i].working(flag_progress)
        if(isCoreEmpty[i]):
            #print('!!!!!!clear!!!!!')
            #print('I want to clear core', i, 'job' , i+1)
            coreList[i].clear()
            break
    count += 1