#Customers can evaluate different items by doing the following steps
c = ()
good = input("Please input the good which you have bought")
while c!= "stop":
        comments = input("Please enter your comments. If you want to continue after entering comments, please press the return key after you enter your comments")
        #input your comments, you add your comments for many times
        my_file = open((good) + ".txt", "w")
        #open the corresponding evaluation file
        my_file.write(comments)
        my_file.write("\n")
        c = input("If you want to stop, please enter stop. If don't, please press the return key")
my_file.close()



# Customers can score items by doing the following steps
my_file = open("points.txt", "w")
points = input("Please enter your points.Please enter the five integers: 1 or 2 or 3 or 4 or 5")
while True:
    if points.isnumeric() == True and int(points) in range(1,6):
        print(points)
        break
    else:
        points = input("Please enter the five integers: 1 or 2 or 3 or 4 or 5")
#
my_file.write("\n")
my_file.write(points)
# write the score to TXT file
my_file.close()
sum = 0
index = 0
f = open("points", "r")
for line in f.readlines():
    sum = int(sum)
    sum = int(line[0]) + sum
    index = index + 1
# reopen the TXT file and sum all the data
print("The sum of all the points is " + str(sum))
average_point = sum / index
# calculate the average
print("The average of the points is " + str(average_point))