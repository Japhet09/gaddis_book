from is_prime import *

def main():
    range_of_nums = range_list()
    prime_list(range_of_nums)


def range_list():
    first_num = input("Enter starting num: ")
    last_num = input("enter last num: ")
    while True:
        if first_num.isdigit() and last_num.isdigit():
            first, last = int(first_num), int(last_num)
            return list(range(first, last))


def prime_list(num_list):
    p_list = []
    for i in num_list:
        if is_prime(i):
            p_list.append(i)
    print("The prime numbers are", p_list, sep = "\n")
    return p_list

main()
