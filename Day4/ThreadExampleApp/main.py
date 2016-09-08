import time, threading

def doLogic(threadName, delay):

    count = 0

    while count < 5:

        print(threadName, 'is running with count', count, 'at', time.ctime(time.time()))

        count += 1

        #sleep for the specified delay
        time.sleep(delay)
    else:
        print('Finished running', threadName)

# normal way to run functions executes them one after another
# doLogic('Thread-1', 3)
# doLogic('Thread-2', 1)


# now we use thread

# to pass multiple functions to a single thread, best to have one fucntion, that will call everything else in the right order

t1 = threading.Thread(target=doLogic, args=('Thread-1', 3))
t2 = threading.Thread(target=doLogic, args=('Thread-2', 1))

t1.start()
t2.start()


doLogic('Thread-3', 5) # runs on the main UI thread
doLogic('Thread-4', 5) # will need to wait for Thread-3 to finish because it runs on the same thread
