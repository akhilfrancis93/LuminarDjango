for row in range(1,6):
    for col in range(1,10):
        if (row==5)|(row+col==6)|(col-row==4):
            print("*",end="\t")
        else:
            print(" ",end="\t")
    print()