def is_prime(num):
    count=0
    if num>1:
        for i in range(2,num//2):
            if num%i==0:
                count+=1
                break
    if count>0: print('not a prime number')
    else: print('is a prime number')

# giving multiple inputs as a list to the function
[is_prime(i) for i in [5,13,9,27,325,23]]
