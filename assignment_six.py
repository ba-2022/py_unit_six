#Betelhem Alemu
#1/19/23
#find duplicate birthdays

import random

''' 
asks the user how many times to run the program and returns that number

'''
def intro():

   number_list = input("how many times do you want this to run?")
   return number_list

def get_birthdays():
    list = []
    for x in range(23):                                             # prints out 23 numbers
        list.append(random.randint(1, 356))                         # ensures that the numbers are between 1 and 365
    return list

''' 
compares the numbers in the list with each other and if they equal each other its a duplicate 

'''
def is_duplicate(list):
    x = 0
    for number in list:
        x += 1
        for othernumber in list[x: -1]:
            if number == othernumber:
                return True


'''
keeps track of the amount of duplicates found

'''
def main():
    counter = 0
    z = int(intro())
    for x in range(z):
        list = get_birthdays()
        if is_duplicate(list) == True:
            counter += 1
    g = int((counter/z) * 100)                                  # turns the amount of duplicates into a percentage
    print("The percent of duplicates found is " + str(g) + "%")





main()



