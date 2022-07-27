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

if __name__ == "__main()__":
    main()

