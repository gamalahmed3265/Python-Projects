import argparse

parse=argparse.ArgumentParser()


def sumNumbers(arr:list):
    results=0
    for i in arr:
        results+=arr[i]
    return results
def mulNumbers(arr:list):
    results=1
    print(arr)
    for i in arr:
        results*=i
    return results
def dividNumbers(arr:list):
    results=1
    for i in arr:
        results/=i
    return results


parse.add_argument("greating",help="this greating message display")
parse.add_argument("-v","--verbosity",type=str,choices=["*","/","+"],help="Detetermines How Much info is display")
parse.add_argument("-n","--numbers",type=int,nargs='*',help="numbers to be added")



args=parse.parse_args()
print("*"*40)
print(args)

if args.verbosity=="+":
    print(sumNumbers(args.numbers))
elif args.verbosity=="*":
    print(mulNumbers(args.numbers))
elif args.verbosity=="/":
    print(dividNumbers(args.numbers))
else:
    print("There Error ")