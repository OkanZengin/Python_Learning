command=""
start=0
stop=0
while True:
    command= input("> ").lower()
    if command=="start" and start==0:
        print("car started ")
        start+=1
        stop=0
    elif command=="stop" and stop==0:
        print("car stopped")
        stop+=1
        start=0
    elif command=="quit":
        print("Bye")
        break
    elif command=="help":
        print('''
Hello. Welcome
To start the car type 'start'
To stop the car type 'stop'
To quit type 'quit'
        ''')
    elif command != "start" and command != "stop" and command != "help":
        print("I don't get that. ")
    elif start>0:
        print("hey, car is already started")
    elif stop>0:
        print("hey, car is already stopped")

input("press enter to quit")