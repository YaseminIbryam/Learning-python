import math

while True:
    rows = int(input("Please enter the number of rows:"))
    if rows % 2 == 0:
        print("Please enter an odd number for symmetric diamond:")
    else:
        break
interval = math.floor(rows/2)
is_middle_reached = False
for asterisk in range(1, rows, 2):
    print(f"{interval * ' '}{asterisk * '*'}{interval * ' '}")
    interval -= 1
for asterisk in range(rows, 0, -2):
    print(f"{interval * ' '}{asterisk * '*'}{interval * ' '}")
    interval += 1


