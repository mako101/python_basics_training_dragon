import time, threading

def doLogic(threadName, delay):

    count = 0

    while count < 5:

        print(threadName, "is running with count", count, "at", time.ctime(time.time()))

        count += 1

        #sleep for the delay
        time.sleep(delay)

    else:
        print("Finished running", threadName)


#normal way to run the function above without thread makes logic run one after the other
# doLogic("Thread-1", 3)
# doLogic("Thread-2", 1)

#now use thread
t1 = threading.Thread(target=doLogic, args=("Thread-1", 3))
t2 = threading.Thread(target=doLogic, args=("Thread-2", 1))

#start both threads
t1.start()
t2.start()

doLogic("Thread-3", 5) #runs on main ui thread
doLogic("Thread-4", 5) #will need to wait for Thread-3 to finish because it runs on main ui thread

# print("Hello")
# count = 0
#
# while count < 5:
#
#     print("hello is running with count", count, "at", time.ctime(time.time()))
#
#     count += 1
#
#     #sleep for the delay
#     time.sleep(5)