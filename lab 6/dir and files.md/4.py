import os

f = open(r"/Users\admin\Desktop\pp2\lab 6\dir and files.md/4.txt")
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")
