def lex(s):
    mylist = list(s)
    flag = 0
    x = 0
    for x in range(len(mylist) - 2, -1, -1):
        if mylist[x+1] > mylist[x]:
            min = 'z'
            ind = 0
            for index, z in enumerate(mylist[x+1:]):
                if mylist[x] < z <= min:
                    min = z
                    ind = x + 1 + index

            temp = mylist[x]
            mylist[x] = mylist[ind]
            mylist[ind] = temp
            flag = 1
            mylist[x+1:] = sorted(mylist[x+1:])
            break
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