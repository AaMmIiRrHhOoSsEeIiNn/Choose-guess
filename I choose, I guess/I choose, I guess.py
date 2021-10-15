




import random

print("\n\nHey! let's play a game. I choose a number and I'll try to geuss it too.")
print("You should give me a range for choosing.\n")
start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))

#choosing a number:
number = random.randint(start_range, end_range)
n_guess = 0

print("\nok I get a number. Now I try to findout it.")
print("Notice that it is between ",start_range,end_range)
print("\n")
print("Number is " + str(number))
print("\n")

while(True):
    n_guess += 1
    geuss_number = int((start_range + end_range)/2)
    print("Guess:"+str(n_guess)+" Number is " + str(geuss_number))
    if(number>geuss_number):
        print("BIGER")
        start_range = geuss_number
    elif(number<geuss_number):
        print("SMALLER")
        end_range = geuss_number
    elif(geuss_number==number):
        print("YEEESS! \nI knew it...\n")
        break
    # And hope you know why we don't need next code:    
    #else:
    #    print("ERROR! TRY RIGHT ANSWER/")
    #    continue




