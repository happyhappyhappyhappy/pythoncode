S=[4,5,6]
FXOR=0
FXOR=(S[0]^S[1])^S[2]
print(f"デフォルトXOR={FXOR}")
# index=0
S01=S.copy()
S02=S.copy()
tmp=S01[0]
S01[0]+=1
FXOR01=FXOR
FXOR01=((FXOR01^S01[0])^S01[1])^S01[2]
FXOR02=FXOR
FXOR02=(FXOR02^tmp)^S01[0]
print(f" 和を足して全追加 {FXOR01} 和を足しただけ {FXOR02}")