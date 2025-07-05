# def main():
#     x = input("Input Your numbers: ")
#     print(reverse_digits(x))


# def reverse_digits(x):
#     while len(x) < 4:
#         x = "0" + x
#     return int(x[::-1])


# main()

def main():
    x = int(input("Input Your numbers: "))
    drawTriangle(x)


def drawTriangle(x) :
    print("*")
    for i in range(1,x):
        j = i+1
        if(i == x - 1):
            for n in range(j):
                    print("*", end=" ")
        else:
            for n in range(j*2-1):
                if(n == 0 or n == j*2-2):
                    print("*", end="")
                else :
                    print(".", end="")
        print()

main()
