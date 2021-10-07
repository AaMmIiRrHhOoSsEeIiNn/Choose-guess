
#Now it's on you to choose a number and computer guess it!

print("\n\nHey! let's play a game. You choose a number and I try to geuss it.\n")
print("First please take me a range of your number:")

start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))

input(" Now select a number and keep it in your mind. Whenever you were ready, press any key to continue:\n ->")
print("Ok . Now I ask some questions and you help me to guess.")
print("If your number is Bigger, enter 'B'.")
print("If your number is Smaller, enter 'S'.")
print("If I Geuss your number, enter '0'.\n")

n_guess = 0
while(True):
    n_guess += 1
    geuss_number = int((start_range + end_range)/2)
    
    print("Guess:"+str(n_guess)+" Your number is " + str(geuss_number))
    input_answer = input("\t -> ")
    input_answer = input_answer.upper()
    
    if(input_answer=="B"):
        start_range = geuss_number
    elif(input_answer=="S"):
        end_range = geuss_number
    elif(input_answer=="Y"):
        print("YEEESS! I knew it...\n")
        break
    else:
        print("ERROR! TRY RIGHT ANSWER/")
        continue


