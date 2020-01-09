# Problem https://atcoder.jp/contests/abc082/tasks/abc082_b
# Python 3rd Try

yes = "Yes"
no = "No"

def solver(sStr,tStr):
    ssStr = ''.join(sorted(sStr))
    srtStr = ''.join(sorted(tStr,reverse=True))
    result = yes if ssStr < srtStr else no
    return result

if __name__ == "__main__":
    s = input()
    t = input()
    answer = solver(s,t)
    print(answer)

