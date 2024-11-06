def sum_digits(num):

    sum = 0

    while num!=0:

        rem = num % 10

        sum += rem

        num //= 10

    return sum



num = int(input("Enter a number: "))

res = sum_digits(num)

print("Sum of digits: ",res)