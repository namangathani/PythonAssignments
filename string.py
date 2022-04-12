#string
print("Hello")
print('Hello')


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


#space remove
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#string capatalize
txt = "hello, am anusha."

x = txt.capitalize()

print (x)


#case fold
txt = "Hello, Am Anusha!"

x = txt.casefold()

print(x)


#string center
txt = "anusha"

x = txt.center(20)

print(x)


#count
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


#encode
txt = "My name is anusha"

x = txt.encode()

print(x)


#find
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)