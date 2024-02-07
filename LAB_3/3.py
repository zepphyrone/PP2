heads = int(input())
legs = int(input())
def solve(numheads, numlegs):
    
    rabbits = int((numlegs - numheads * 2)/2)
    chickens = int(numheads - rabbits)
    print("The amount of rabbits: ", rabbits)
    print("The amount of chickens: ", chickens)