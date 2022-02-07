weight = [8,7,14,9,6,9,5,15,6,7,8]
n = 11
capacity = 20
bins = [[8]]
num_index = 0

def recursive(number, bin_order):
    global num_index
    if num_index > 10:
        print("Finished")
    else:
        #bin_sum = bins[bin_order] + number
        bin_sum = 0
        for num in bins[bin_order]:
            bin_sum += num
        bin_sum += number
        print(bin_sum)
        if bin_sum <= capacity:
            bins[bin_order].append(number)
            num_index += 1
            recursive(weight[num_index], 0)
        else:
            recursive(number, bin_order + 1)
    
recursive(7, 0)
