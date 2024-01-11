# base.pyの次の部分を借用
print("".join(map(str,Othello)))
# ↓ submit01.pyを個人で書き直した内容
strList=[]
for j in range(0,N):
    strList.append(str(Acc[j]%2))
print("".join(strList))
# 実はjoinはリスト引数1個で出来たわけだ
