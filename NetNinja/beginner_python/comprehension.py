# double the prize list elements
prizes = [5, 10, 50, 100, 1000]

# with a for loop
dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

# with comprehension method, declaration/assignement/logic in 1 line!
dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)

# ---------------------------------------------------
# squaring numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using a for loop
squared_even_nums = []
for num in nums:
    if(num**2) % 2 == 0:
        squared_even_nums.append(num**2)
print(squared_even_nums)

# comprehension method
squared_even_nums = [num**2 for num in nums if(num**2) % 2 == 0]
print(squared_even_nums)
