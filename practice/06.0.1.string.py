# string - represents string
    # can convert any other data type into string by str()
my_str = 10;
to_string = str(my_str);
print(to_string)


#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = tet[2:5] # llo

b = "Hello, World!"
print(b[:5]) #Hello


b = "Hello, World!"
print(b[2:]) #llo, World!

b = "Hello, World!"
print(b[-5:-2]) #orl


a = "Hello, World!"
print(a.upper()) #HELLO, WORLD!


a = "Hello, World!"
print(a.lower()) #hello, world!

a = " Hello, World! "
print(a.strip()) # "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J")) #Jello, World!

#replaces all "H" in the string
a = "Hello, Harold!"
print(a.replace("H", "J")) #Jello, Jarold!

a = "Hello, World!"
print(a.split(",")) #['Hello', ' World!']

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 59.00 dollars

# Display the price with 2 decimals with rounded number
# :2f will automatically rounds the number to 53.14
price = 59.139
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 59.14 dollars

# Fstring can do math also
txt = f"The price is {20 * 59} dollars"
print(txt) #The price is 1180 dollars


# index will return starting index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) # 7

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.index("e", 8) #13
print(x)


# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

# converting to title case
def format_name(data) :
    return data.title()
to_title = format_name("i'm Naveen, i live in the London right now")
print(to_title) # I'M Naveen, I Live In The London Right Now


# escape sequence
txt = "We are the so-called \"Vikings\" from the north."


# Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

message = input("Please enter the message : ")
#split will take string and replace with "", which will covert into array
words = message.split(" ")
new_message = ''

data = {
    ':)':'😀',
    ':(':'😟'
}
for word in words:
    new_message+= data.get(word,word) +' '
print(new_message)

# checking the string in the sentence
txt = "The best things in life are free !"

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
else :
    print("expensive is present in the sentence")
