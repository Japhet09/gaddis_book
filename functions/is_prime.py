def main():
    n = int(input("Number: "))
    if is_prime(n):
        print("the number is prime")
    else:
       print("The number is not prime")
    
      
    
def is_prime(num):
    prime = True
    for i in range(2,num):
        if num%i ==0:
            prime = False
            break
    return prime

# The code under the conditional will only get called
# upon when is_prime.py is execeted as python not when
# is imported  as a module in another script
if __name__ == "__main()__":
    main()

