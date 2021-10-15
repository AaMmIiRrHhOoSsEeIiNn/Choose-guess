



import random



print("\n\nHey! let's play a game. I choose a number and you try to geuss it.")
print("You should give me a range for choosing.\n")
start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))

#choosing a number:
number = random.randint(start_range, end_range)
n_guess = 0
print("\nok I get a nunber. Now try to findout it. I help you too...")
print("Notice that it is between ",start_range,end_range)

while(True):
    n_guess+=1
    print("geuss "+str(n_guess))
    geuss_number = int(input("Enter your number:\n\t ->"))
    if(geuss_number<number):
        print("\tNO, it's bigger.\n")
    elif(geuss_number>number):
        print("\tNo, it's smaller.\n")
    else:
        print("\tYEEEESSSS! you shot it babe...\n\n")
        break
    
