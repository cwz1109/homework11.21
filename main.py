# ask for x and n
x=int(input("Give me a x:"))
n=int(input("Give me a n:"))
# calculate the answer
Q=x**n
for n in range(n):
    print(x)
print("=",Q)

quit()

# set the n = 1 first
n=1
# set the x = 0 first
x=0
# define a function that N = 1/(n^2)
N=1/(n**2)
# let N + x to make a cycle
x=N+x
# set the condition
while not N<0.0000000001:
    print(x)
# make a cycle
    n+=1
quit()