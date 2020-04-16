# using choice() function from random to play 749 Max lottery
import sys

from random import choice


try:
    n = int(input("Please input total number for draw:"))
    m = int(input("How many draws do you want?"))

    if n <= 0 or m <= 0 or m > n:
        sys.exit("The number is wrong!")
    

except ValueError:
    print("You must input integer number!")

else:
    
    num_lists = list(range(1,n+1))

    i = 1
    selected_nums = []
    selected_num = 0

    while i <= m:
        selected_num = choice(num_lists)
        selected_nums.append(selected_num)
        num_lists.remove(selected_num)
        i += 1

    print(sorted(selected_nums))
