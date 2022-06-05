import sys

if len(sys.argv)!=2:
    print('One command line parameter must be provided.')
    quit()

try:
    inf=open(sys.argv[1],"r")

    lines=[]
    for line in inf:
        lines.append(line)
        if len(lines)>10:
            lines.pop(0)
    inf.close()

except:
    print('An error has occurred.')
    quit()

for line in lines:
    print(line, end='')
