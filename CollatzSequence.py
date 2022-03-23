from pylab import *

user_max = int(input("Enter a max: "))

count = 0 
prev = user_max 

if user_max < 2:
    exit()

#Collatz
while user_max > 1: 
    if user_max % 2 == 0:
        user_max = user_max/2
        count += 1
    else:
        user_max = 3 * user_max + 1
        count += 1

    plot([count - 1, count], [prev, user_max], '-ob')
    prev = user_max

title(f"Collatz Sequence")
xlabel(f"Stopping Points: {count + 1}")
savefig(f"Collatz.png",bbox_inches="tight",dpi=600)
show()