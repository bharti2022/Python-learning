import argparse,sys

parser = argparse.ArgumentParser(
         description="A custom simple argument parser",
         epilog="This is where you might put example usage"
     )
 
parser.add_argument("filename",help="action")
arg = parser.parse_args()
print(arg._get_args())
n = len(sys.argv)
print("total no of args : ", n)

print("args are")
for i in range(1, n):
    print(sys.argv[i],end=" ")
    
    
Sum = 0

for i in range(1, n):
    Sum+=int(sys.argv[i])    

print("'\n\nResult", Sum)

