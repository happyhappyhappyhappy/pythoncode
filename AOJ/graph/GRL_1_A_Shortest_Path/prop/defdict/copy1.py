from collections import defaultdict

my_dict=defaultdict(list)
key_list = ["りんご","みかん","ばなな"]
x = 0
for key in key_list:
    my_dict[key].append(x)
    x=x+1
for key in key_list:
    print(f"{key}-> {my_dict[key]}")
