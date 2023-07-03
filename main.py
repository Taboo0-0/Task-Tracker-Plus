tcount = 0
data = 'data.txt'

# Starts File so that when the defines is reran file does not restart.
with open(data, 'w', encoding='utf-8') as my_file:
            my_file.write("")


def taskcreate():
    que = input("New task?,(Yes or yes) ")
    global tcount
    if que == "Yes" or que == "yes":
        with open(data, 'a', encoding='utf-8') as my_file:
            my_file.write(input("What Task? "))
        with open(data, 'a', encoding='utf-8') as my_file:
            my_file.write((", ") + (input("Priority?(H,M,L) ")))
        with open(data, 'a', encoding='utf-8') as my_file:
            my_file.write((", ") + (input("When Due?(Format 00:00 + Day) ")) + "\n")
        tcount = tcount + 1 
        ask()
    else:
         print("Retry!")
         taskcreate()



def fileprint():
    f = open(r" ##file loc ", 'r')
    content = f.read()
    print("\n" + content)
    f.close()
    ask()


def ask():
     option = int(input("Would you like to add task?(1), or would you like to view tasks?(2): "))
     if option == 1:
          taskcreate()
     elif option == 2:
          fileprint()
     else:
        print("Invalid! Try again!")
        ask()

ask()
