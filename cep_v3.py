#import multiprocessing
import threading
import time
a = threading.Semaphore()
b = threading.Semaphore()
c = threading.Semaphore()
d = threading.Semaphore()
#e = threading.Semaphore()


chair_total = int(input("Enter total number of chairs: ")) 
chair_used = int(input("Enter number of chair used: ")) 
barber_chair = input("Enter status of barber's chair: ")#True = occupied bool variable


print("chair_total: ",chair_total)  
print("chair_used: ",chair_used)  
print("barber_chair: ",barber_chair) 

#barber_chair #1 means occupied/false
barber_sleep=0 #0 means barber is awake 

def customer():
    #global chair_total
    global chair_used
    #global barber_chair

    while chair_used<=chair_total:
        if (barber_chair==True and chair_used < chair_total):
            chair_used+=1
            #time.sleep(5)
            b.release()
            print("%s released lock"%(threading.current_thread().name))
            print("semaphore b value: ",b._value)
            time.sleep(5)
            print("Chairs used",chair_used)
        elif (chair_used==chair_total and barber_chair==True):
            #time.sleep(5)
            c.release()#Semsignal(c)
            #print("semaphore c",c)
            print("%s released lock"%(threading.current_thread().name))
            print("semaphore c value: ",c._value)
            balk()
            d.release()
            print("%s released lock"%(threading.current_thread().name))
            print("semaphore d value: ",d._value)
            break
        else:
            #time.sleep(5)
            #print("releasing semaphore a")
            a.release() #Semsignal(a) +1
            #print("semaphore a",a)
            print("%s released lock"%(threading.current_thread().name))
            print("semaphore a value: ",a._value)
            getHaircut()
            break

def cutHair():
    global barber_chair
    #print("acquiring semaphore b")
    #b.acquire()#semWait(b)
    #b.acquire()
    #print("semaphore b",b)
    #print("%s acquire lock"%(threading.current_thread().name))
    #print("semaphore b value: ",b._value)
    if(barber_chair==True):
       print("Barber's chair occupied ")
   
    elif(barber_chair==False):
       print("Barber's chair empty")
       #print("%s release lock"%(threading.current_thread().name))
       #print("semaphore e value: ",e._value)


def getHaircut():
    #global chair_total
    global chair_used
    global barber_chair
    #global barber_chair
    #print("aquiring semaphore")
    a.acquire() #semWait(a) -1
    print("%s acquired lock"%(threading.current_thread().name))
    print("semaphore a value: ",a._value)
    barber_chair=True
    if(barber_chair==True and chair_used==0):
        pass
    else:
        print("Barber's chair status :",barber_chair)
    #b.release()
    #time.sleep(1)
    #print("%s released lock"%(threading.current_thread().name))
    #print("semaphore b value: ",b._value)
    d.acquire()
    b.acquire()
    if(chair_used==0):
        pass
    else:
        #barber_chair=False
        #time.sleep(1)
        #print("%s acquired lock"%(threading.current_thread().name))
        #print("semaphore e value: ",e._value)
        chair_used-=1
    print("%s acquired lock"%(threading.current_thread().name))
    print("semaphore d value: ",d._value)
    print("semaphore b value: ",b._value)
    print("Chairs used: ",chair_used)
    customer()


def barber():
    if(chair_used!=0 and barber_chair==False):
        barber_sleep=0
        #time.sleep(5)
        #b.release()
        #print("semaphore b",b)
        #print("%s released lock"%(threading.current_thread().name))
        #print("semaphore b value: ",b._value)
        cutHair()
    elif(barber_chair==True):
        pass
    elif(barber_chair==False and chair_used==0):
        barber_sleep=1
        print("barber has gone to sleep")
        #time.sleep(5)

def balk():
    c.acquire()#////////////////////sem wait(c)
    #print("semaphore c:",c)
    print("%s acquired lock"%(threading.current_thread().name))
    print("semaphore c value: ",c._value)
    if(chair_used==0):
       pass
    elif(chair_used==chair_total):
        time.sleep(1) 
        print("Unattended customer has left shop")

def main():
    
     


    # start=time.clock()
    #p1=multiprocessing.Process(target=customer)
    #p2=multiprocessing.Process(target=cutHair)
    #p3=multiprocessing.Process(target=getHaircut)
    #p4=multiprocessing.Process(target=barber)
    #p5=multiprocessing.Process(target=balk)

    #p1.start()
    #p2.start()
    #p3.start()
    #p4.start()
    #p5.start()

    #p5.join()
    #p2.join()
    #p3.join()
    #p4.join()
    #p5.join()
    t1 = threading.Thread(target = customer)
    t2 = threading.Thread(target = getHaircut)
    t3 = threading.Thread(target = cutHair)
    t4 = threading.Thread(target = barber)
    t5 = threading.Thread(target = balk)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print("All Threads done Exiting")


    # finish=time.clock()
    # x=finish-start
    # print("time = ",x)
    #print(f'Finished in{round(finish-start,2)}seconds')
main()