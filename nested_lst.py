if __name__ == '__main__':
    lst=[]
    s=0
    for i in range(int(input())):
        name = str(input())
        score = int(input())     
        lst.append([name,score])
        lst=set()
    print(lst)       