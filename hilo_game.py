import random 
sec_num = random.randint(1, 13)
for x in range(2):
    x = int(input("Enter a number: "))
    if x < sec_num:
        print("Its to low")
        continue
    elif x > sec_num:
        print("its too high")
        continue
    elif x == sec_num:
        print("Congratulations! you won")
        break