# Find a string
# https://www.hackerrank.com/challenges/find-a-string

def count_substring(string, sub_string):
    a=len(sub_string)
    c=0
    l = len(string)
    for i in range(l-a+1):
        b = string[i:i+a]
        if b == sub_string:
            c+=1
    return c
