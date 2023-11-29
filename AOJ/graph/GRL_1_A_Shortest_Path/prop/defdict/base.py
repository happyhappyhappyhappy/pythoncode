from collections import defaultdict

# defaultdictを作成し、デフォルト値を空のリストに設定
my_dict = defaultdict(list)

# キーがリスト型の例
key_list = ['apple', 'orange', 'banana']

# リスト型のキーを使用して値を追加
for key in key_list:
    my_dict[key].append('value')

# デフォルト値（空のリスト）を表示
print(my_dict.default_factory)  # <class 'list'>

# 結果を表示
print(my_dict)
