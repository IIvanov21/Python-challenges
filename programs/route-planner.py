from typing import NoReturn


def route_planner(number_string:str):
    numbers=list(map(int, number_string.split()))
    route=[0]
    temp=[]
    route.append(numbers[0])
    for i in range(len(numbers)):
        if route[-1]>numbers[i]:continue
        for j in range(5):
            if numbers[-1]!= numbers[i]: temp.append(numbers[i+j]) 
        temp.sort()
        print(*temp)
        for k in temp:
            if route[-1]<k: 
                route.append(k)
                temp.clear()
                break   
    route.append(numbers[-1])
    route=dict.fromkeys(list(route))
    return route.keys()

print(route_planner("0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15"))

    

