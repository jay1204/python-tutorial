## Creater: Zexi Chen(zchen22)


"""
The code from the question
"""
def num_digits(x):
  return len(str(x))

def most_digits(L):
  L = sorted(L, key=num_digits)
  return L[-1]

def largest_two_digit_even(L):
  two_digit_numbers = [i for i in L if num_digits(i)==2]
  evens = [i for i in two_digit_numbers if i%2==0]
  evens.sort()
  return evens[-1]

def best(L, criteria):
  return criteria(L)


# Prints 1
# Prints 84
# Prints 1023
"""
This function takes a single integer(10 base) as input and 
return the number of ones in that number
"""
def num_ones_in_binary(num):
	bin_str = bin(num)
	count =0
	for i in bin_str:
		if i == '1':
			count += 1

	return count

"""
This function takes a list of integers(10 base) as input and 
return integer from that list that has the most ones in binary
"""
def most_ones_in_binary(L):
  result = 0
  most_one = 0
  for num in L:
    count = num_ones_in_binary(num)
    if count > most_one:
      result = num
      most_one = count

  return result

def main():
  L = [1, 76, 84, 95, 214, 1023, 511, 32]
  print(best(L, min))
  print(best(L, largest_two_digit_even))
  print(best(L, most_digits))
  print(best(L,most_ones_in_binary))

if __name__ == '__main__':
	main()