#Python Pre Work

#Question 1
def hello(name):
    print("Hello " + name.upper()+ "!")

hello('christian')

#Question 2
def odd_numbers():
	numbers = list(range(0, 100))
	for number in numbers:
		if number % 2 != 0:
			print(number)
        
odd_numbers()

#Question 3
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([19,7,3,26,2])
print(max_num_in_list([19,7,3,26,2]))

#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')

is_leap_year(2013)


#Question 5
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

