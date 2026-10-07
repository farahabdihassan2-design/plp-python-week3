count = 1
# BUG: Fixed initial value of total from 8 to 0 so the sum starts correctly
total = 0

# BUG: Changed count < 5 to count <= 5 so the loop includes 5 to equal 15
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Fixed TypeError by converting integer total to string using str()
print("Sum of 1 to 5 is: " + str(total))