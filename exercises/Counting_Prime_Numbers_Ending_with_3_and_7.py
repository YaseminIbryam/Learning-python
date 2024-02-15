prime_list = [2]
prime_counter = 0
number = 3
while prime_counter < 10000:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            number += 1
            is_prime = False
            break
    if is_prime:
        prime_list.append(number)
        prime_counter += 1
        number += 1

searched_number_count = 0
for num in prime_list:
    if str(num).startswith("3") and str(num).endswith("7"):
        searched_number_count += 1
print(searched_number_count)





        

        
         
        



