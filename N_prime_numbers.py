#2 N prime numbers

    
count = 0
num = 2

n = int(input("Enter how many prime numbers you want: "))

while count < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        count += 1

    num += 1




    




            
# num=int(input("Enter a number="))

# if num<=1:
#     print(f"number {num} is not a prime number")

#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is a prime number ")
#         else:
#             print(num,"is not a prime number")