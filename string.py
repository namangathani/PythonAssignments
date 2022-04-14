#string
print("Hello")
print('Hello')

#string capatalize
txt = "python is FUN!"
x = txt.capitalize()
print (x)


#case fold
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#string center
txt = "banana"
x = txt.center(20)
print(x)

#count
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode
txt = "My name is Ståle"
x = txt.encode()
print(x)

#endswith
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#expandtabs
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

#find
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#slicing string
b = "Hello, World!"
print(b[2:5])

#upper case strings
a = "Hello, World!"
print(a.upper())

#lower case strings
a = "Hello, World!"
print(a.lower())

#string concatenate
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#format string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#index of a word
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)

#alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)

#ascii
txt = "Company123"
x = txt.isascii()
print(x)

#decimal
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

#digit
txt = "50800"
x = txt.isdigit()
print(x)

#identifier
txt = "Demo"
x = txt.isidentifier()
print(x)

#isLower
txt = "hello world!"
x = txt.islower()
print(x)

#numeric
txt = "565543"
x = txt.isnumeric()
print(x)

#printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

#isSpace
txt = "   "
x = txt.isspace()
print(x)

#isTitle
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#isUpper
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
