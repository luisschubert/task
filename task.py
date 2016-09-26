import time, re, os, datetime

# DATA STRUCTURES
startTimes = {}  # dictionary of name and startTime in unixtime
recentTasks = []  # list of strings


# PROGRAM FUNCTIONS
def printTasks():
    print ' - tasks - '
    i = 0
    for task in startTimes:
        print str(i) + '\t' + task
        i += 1


def printRecentTasks():
    print ' - recent tasks - '
    i = 0
    for task in recentTasks:
        print str(i) + '\t' + task


def updateRecentList(taskName):
    i = 0
    updating = False
    for task in recentTasks:
        if task == taskName:
            recentTasks.pop(i)
            recentTasks.insert(0,taskName)
            updating = True
        i += 1
    if not updating:
        recentTasks.insert(0, taskName)
    if len(recentTasks) > 10:
        recentTasks.pop(10)


def saveToLog(totalTime, taskName, startTime, endTime):
    f = open("/users/luisschubert/Documents/taskER/log.txt", "a")
    formatStartTime = datetime.datetime.fromtimestamp(int(startTime)).strftime('%Y-%m-%d %H:%M:%S')
    formatEndTime = datetime.datetime.fromtimestamp(int(endTime)).strftime('%Y-%m-%d %H:%M:%S')
    logLine = taskName + '\t' + str(totalTime) + '\t' + formatStartTime + '\t' + formatEndTime + '\n'
    f.write(logLine)


def startTask(taskName):
    if startTimes.has_key(taskName):
        print "You're already doing that... ya dingus"
    else:
        startTimes[taskName] = time.time()


def endTask(taskName):
    if len(startTimes) == 0:
        print "You ain't doin shit dawg"
    else:
        startTime = startTimes[taskName]
        endTime = time.time()
        totalTime = endTime - startTime
        saveToLog(totalTime, taskName, startTime, endTime)


# PROGRAM BODY
running = True

while running:
    os.system("clear")
    printTasks()
    command = raw_input("...")
    if command == "quit":
        running = False
    elif command == "start":
        os.system("clear")
        printRecentTasks()
        command = raw_input("\tstart\n\t..?")
        num = len(recentTasks)
        pattern = "[0-" + str(num) +"]"
        if re.match(pattern, command) and len(recentTasks) != 0:
            taskName = recentTasks.pop(int(command))
        else:
            taskName = command
        updateRecentList(taskName)
        startTask(taskName)
    elif command == "end":
        os.system("clear")
        printTasks()
        command = raw_input("\tend\n\t..?")
        endTask(command)
        # startTimes data type needs to be changed to something else to use indexing
        # num = len(startTimes)
        # pattern = "[0-" + num + "]"
        # if re.match(pattern, command) and len(startTimes) != 0:
        #     taskName = startTimes.get

