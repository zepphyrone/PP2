import os

def pathh (path):
    print([name for name in os.listdir(path)]) 
    print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]) 
    print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]) 
    
path = r"\Users\Aisha\Desktop"
pathh(path)
