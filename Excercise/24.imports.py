
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

