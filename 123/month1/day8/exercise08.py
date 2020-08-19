def descending_order_of_list(list):
    for r in range(len(list) - 1):
        for c in range(r + 1, len(list)):
            if list[r] < list[c]:
                list[r], list[c] = list[c], list[r]

list01=[43,2,45,65,76,8,9]
descending_order_of_list(list01)
print(list01)

