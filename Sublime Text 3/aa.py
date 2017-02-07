def count_substring(string, sub_string):
    a=len(sub_string)
    c=0
    for i in range(0,len(string)):
        for j in range(len(sub_string),len(string)):
            b=string[i:j]
            if(sub_string is b):
                c=c+1
            else:
                continue
    print(c)
