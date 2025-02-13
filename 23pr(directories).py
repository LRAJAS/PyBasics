from pathlib import Path 
#path = Path("e-commerce")
#print(path.mkdir())
#print(path.rmdir())
#print(path.open())
path  = Path()
for file in path.glob('*'):
    print(file)
