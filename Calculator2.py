print('welcome to my calculator!')
end=input('press enter if you want to use this tool ')
end=input('please enter your command (+,-):')
print('you have selected : ',end)
num1=int(input("please enter your first number : "))
num2=int(input("please enter your second number : "))

if end=='+':
    print("your answer is : ", num1+num2)
elif end=='-':
    print("your answer is : ", num1-num2)