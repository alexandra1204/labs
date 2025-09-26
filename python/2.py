# n = 4
# tr = []
# for i in range(n):
#     row = [1] * (i + 1)
#     tr.append(row)
#     for j in range(1, i):
#         tr[i][j] = tr[i-1][j-1] + tr[i-1][j]
# k=n
# for row in tr:
#     print(k*" ",*row)
#     k-=1



n = 64
tr = [[1] * (i+1) for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        tr[i][j] = tr[i-1][j-1] + tr[i-1][j]
tr2=[]
for row in tr:
    row2=''

    for num in row:

        if num % 2 == 0:
            row2+="  "
        else:
            row2+=" *"
    tr2.append(row2)
k=n
for row2 in tr2:
    print(k*" ",row2)
    k-=1