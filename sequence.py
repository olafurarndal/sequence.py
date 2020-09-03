sequence_length = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 1
n2 = 2
n3 = 3

count = 3

if sequence_length <= 0:
    print("Please enter a positive numer")
elif sequence_length == 1:
    print(n1)
elif sequence_length == 2:
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    print(n3)
    while count < sequence_length:
        total = n1 + n2 + n3
        print(total)
        #update values
        n1 = n2
        n2 = n3
        n3 = total
        count += 1






