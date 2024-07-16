
# ----------------------------------------------------------------
# can import compete file like below
import art, converter

# then access the variables inside the file by module name and then the variable name
print(art.logo)
print(converter.pounds_to_kg(20))

# ----------------------------------------------------------------
# can import individual function like below
from converter import pounds_to_kg, kg_to_pounds
print(pounds_to_kg(20))
print(kg_to_pounds(20))



# ----------------------------------------------------------------
# function to return largest number int he list
from utils import find_max

numbers = [10, 2, 30, 44, 55, 91, 16, 34, 56, 67, 23]
find_max(numbers)
