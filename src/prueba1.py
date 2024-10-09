def mayor(num1, num2):
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2 
    if num1 == num2:
        return "0"
def main():
    print("Dame un número")
    num1= float(input())
    print("Dame otro")
    num2= float(input())
    print(mayor(num1,num2))

if __name__ == "__main__":
    main()