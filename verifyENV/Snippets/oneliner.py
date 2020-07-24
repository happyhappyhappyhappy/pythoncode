# 1行プログラムのコレクション
# 参考 https://towardsdatascience.com/become-a-python-one-liners-specialist-8c8599d6f9c5
# 以下インポート文

# (1)2変数の交換
print("#1 Swapping the value of 2 variables")
a = 10
b = 5

print("a = {}/ b = {}".format(a, b))

b, a = a, b # Key

print("a = {}/ b = {}".format(a, b))

# (2)List 作成/フィルタ

print("#2 List comprehension")
a = int(input("list len="))

ls = [ j for j in range(0, a)] # Key

print("List = {}".format(ls))

ls = [0 , -1 , 2 , -3 , 4 , -5]
print("List2={}".format(ls))

ls = [ j for j in ls if j > 0] # Key

print("List2Filter={}".format(ls))

# (3) Map
print("#3 Map")
char_list = ["1", "2", "3" , "4"]
print("char_list= {}".format(char_list))

number_list = list(map(int, char_list)) # Key

print("number_list={}".format(number_list))
