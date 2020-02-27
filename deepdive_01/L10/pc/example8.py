import argparse


parser = argparse.ArgumentParser(description='Prints the squares of a list of numbers,and the cubes of another list of number')

parser.add_argument('--sq',help='list of numbers to square',nargs='*',type=float)
parser.add_argument('--cu',help='list of numbers to cube',nargs='+',type=float,required=True,dest = 'cubes')

args = parser.parse_args()

#if args.sq is not None and le(args.sq)>0:    ===   if args.sq    in  Python

if args.sq:
    squares= [n**2 for n in args.sq]
    print(squares)

cubes = [n**3 for n in args.cubes]
print(cubes)

