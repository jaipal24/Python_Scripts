#Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers.

if __name__=='__main__':
    #Reading two values from user
    num1=input("Enter First Number:")
    num2=input("\nEnter Second Number:")
    #Adding those two numbers
    sum=float(num1)+float(num2)
    #Displaying the output
    print("The sum of {0} and {1} is : {2}".format(num1,num2,round(sum,2)))
