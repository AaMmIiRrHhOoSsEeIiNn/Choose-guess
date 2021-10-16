


import random

start_range_o = int(input("Enter start of range: "))
end_range_o = int(input("Enter end of range: "))
# Choosing a number:
guess_list = []
n_repeat = int(input("Enter how many times process repeat?\n ->"))
print("\n")

for i in range(n_repeat):

    start_range = start_range_o
    end_range = end_range_o
    print("Repeat:"+str(i+1))
    number = random.randint(start_range, end_range)
    n_guess = 0
    print("Random Number is " + str(number))
    
    while(True):
        n_guess += 1
        geuss_number = int((start_range + end_range)/2)
        print("Guess:"+str(n_guess)+" ->> " + str(geuss_number))

        if(number>geuss_number):
            start_range = geuss_number

        elif(number<geuss_number):
            end_range = geuss_number

        elif(geuss_number==number):
            print("FOUND.\n")
            guess_list.append(n_guess)
            break
        

# Min and max
print( sorted(list(guess_list)) )
print( "MAXIMUM:" + str(max(guess_list)) )
print( "MINIMUM:" + str(min(guess_list)) )


