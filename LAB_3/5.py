from itertools import permutations 
def print_permutations():
    string = input()
    perm = permutations(string)
    
    for i in list(perm): 
        print (i) 

print_permutations()