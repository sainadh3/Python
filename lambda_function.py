def tables(n):
    return lambda x:x*n
x=int(input())
f1=tables(x)
for i in range(1,11):
    print(f'{x} x {i} = {f1(i)}')

print('***'*10)
def make_incrementor(n):
    return lambda x: x + n

f2 = make_incrementor(42)
print(f2(0),f2(1))