import re

sum = 0
count = 0

fhand = open("regex_sum_1853426.txt")
for line in fhand:
    line = line.rstrip()
    num_list = re.findall( "[0-9]+", line)
    for num in num_list:
        sum = sum + float(num)
        count = count + 1

print("Tong", sum)
print("SL =", count)
