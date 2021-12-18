# This is a sample Python script.
# Python3 code to demonstrate working of
# Convert numeric words to numbers
# Using join() + split()

help_dict = {
	'a': '1',
	'b': '2',
	'c': '3',
	'd': '4',
	'e': '5',
	'f': '6',
	'g': '7',
	'h': '8',
	'i': '9',
	'j': '0'
}

# initializing string
test_str = "a b c d e f "

# printing original string
print("The original string is : " + test_str)

# Convert numeric words to numbers
# Using join() + split()
res = ''.join(help_dict[ele] for ele in test_str.split())
x = int(res)
# printing result
print(x+1000)
