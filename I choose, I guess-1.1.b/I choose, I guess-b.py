



import numpy as np
import time
import random



# Choosing a number:
start_time = time.time()
guess_list_min = []
guess_list_max = []
range_list = []  # end_range_o save for each n_data in this; 
guess_list = []  # Number of guess to find the RandomNumber for each repeatition;
n_data = 3  # n_data: Number of MAX/MIN geusses (n_data for MAX and n_data for MIN) (DETERMINE)
end_range_o = 0  # End of range for start
base_repeat = 0  

for  data in range(n_data): # Total data (in this loop we add step range(end_range_o) and and step repeatirion(base_repaet) to last ones;
    print("Data pack: "+str(data+1))
    base_repeat += 5   # In each n_data we add base_repeat more to repeats variables. (DETERMINE)
    end_range_o += 100  # For each n_data, range increase as much as this.(DETERMINE)
    range_list.append(end_range_o)  # Save range of each repeatition.

    for repeat in range(base_repeat): # Repeat loop (this loop choose a random number (range is canstant))
        start_range = 1
        end_range = end_range_o
        number = random.randint(start_range, end_range)
        n_guess = 0
        print("Repeat: "+str(repeat+1))
        print("Number is " + str(number))
    
        while(True): # Guess loop (this loop try to guess the RandomNumber)
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
    print("END dPack: "+str(data+1)+'\n\n')

    #min and max
    guess_list_max.append(max(guess_list)) # Get MAX for each range in each n_data
    guess_list_min.append(min(guess_list)) # Get MIN too;

print("\nData ranges: ")
for i in range(n_data):
    print(range_list[i])
print("\nMaximum guess list: ")
for j in range(n_data):
    print(guess_list_max[j])
print("\nMinimum guess list: ")
for k in range(n_data):
    print(guess_list_min[k])
print("\n")

print("total time: "+ str(time.time()-start_time))



