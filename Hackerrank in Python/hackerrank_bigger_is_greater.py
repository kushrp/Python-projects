def lex(s):
    mylist = list(s)
    previ = len(mylist) - 1
    flag = 0
    for x in range(len(mylist) - 1, -1, -1):
        s = mylist[previ]
        q = mylist[x]
        if mylist[previ] > mylist[x]:
            temp = mylist[x]
            mylist[x] = mylist[previ]
            mylist[previ] = temp
            flag = 1
            mylist[x+1:len(mylist)-1] = sorted(mylist[x+1:len(mylist)-1])
            break
        else :
            previ = x
    if x is 0 and flag == 0:
        return "no answer"
    else:
        return ''.join(mylist)


def main():
    t = int(input())
    for x in range(0, t, 1):
        s = input()
        ans = lex(s)
        print(ans)


if __name__ == "__main__":
    main()