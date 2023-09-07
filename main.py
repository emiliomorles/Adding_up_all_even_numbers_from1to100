
total_even_numbers = 0
for even_number in range(1,101):
  if even_number % 2 == 0:
    even_number = True
  total_even_numbers += even_number
print(total_even_numbers)

print("\n")
print("or")
print("\n")

total_even_numbers = 0
for even_number in range(2, 101, 2): #I can save 2 lines of code in this way range(2, 101, 2)
  total_even_numbers += even_number
print(total_even_numbers)