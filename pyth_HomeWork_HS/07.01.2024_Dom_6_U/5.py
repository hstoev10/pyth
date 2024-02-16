# list ot 4isla 1,2,3,3,4 , funkciq da izvadi unikalnite elementi

input_list = [1, 2, 3, 3, 3, 4]
duplicates = []

for item in input_list:
    if input_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print(duplicates)
