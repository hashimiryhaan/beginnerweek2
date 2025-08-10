food=["burgerr","biriyani","mandhi","dosa"]
n=len(food)
print("What I eat in a day :)")
for i in range(n):
    for j in range(0,n-i-1):
        if(len(food[j])>len(food[j+1])):
            food[j],food[j+1]=food[j+1],food[j]
print("Breakfast:",food[0])
print("Lunch:",food[1])
print("Snack:",food[2])
print("Dinner:",food[3])