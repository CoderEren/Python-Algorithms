no_of_numbers = int(input("How many numbers would you like to add?\n"))
weight = []
for i in range(no_of_numbers):
    number = float(input("Add a number: "))
    weight.append(number)
n = len(weight)
capacity = float(input("What is the maximum size of each container?\n"))

weight.sort(reverse = True) #sorts the numbers into descending order for a more optimal solution

bins = [[]]
num_index = 0

def recursive(number, bin_order):
    global num_index
    bin_sum = 0
    try:
        for num in bins[bin_order]:
            bin_sum += num
    except: #if bins[bin_order] doesn't exist, this executes
        bins.append([])
    bin_sum += number
    print("Bin Sum: " + str(bin_sum))
    if bin_sum <= capacity:
        bins[bin_order].append(number)
        num_index += 1
        try:
            recursive(weight[num_index], 0)
        except:
            print("No more numbers!")
    else:
        recursive(number, bin_order + 1)
    
recursive(weight[0], 0)

#Example Solution
#If numbers entered are 8, 7, 14, 9, 6, 9, 5, 15, 6, 7, 8
#Then weight = [15.0, 14.0, 9.0, 9.0, 8.0, 8.0, 7.0, 7.0, 6.0, 6.0, 5.0]
#And bins = [[15.0, 5.0], [14.0, 6.0], [9.0, 9.0], [8.0, 8.0], [7.0, 7.0, 6.0]]
#Optimal solution is 5 bins and 5 bins are used so the solution is optimal
