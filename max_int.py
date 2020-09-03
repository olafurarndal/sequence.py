#Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.

max_int = 0

while True:

    num_int = int(input("Input a number: "))    # Do not change this line
 

    if num_int >= 0:
        if max_int >= num_int:
            max_int = num_int
    else:
        break
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line

# fá upplýsingar af notandanum
# hækka max_in ef num_int sé hærra
# tékka ef num_int sé negatív tala, ef svo prenta og enda


