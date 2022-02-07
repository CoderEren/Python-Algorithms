#The bin packing problem is an optimization problem, in which items of different sizes 
#must be packed into a finite number of bins or containers, each of a fixed given capacity, 
#in a way that minimizes the number of bins used.

no_of_numbers = int(input("How many numbers would you like to add?\n"))
weight = []
for i in range(no_of_numbers):
    number = float(input("Add a number: "))
    weight.append(number)
n = len(weight)
capacity = float(input("What is the maximum size of each container?\n"))

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
