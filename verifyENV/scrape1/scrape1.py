import requests
from bs4 import BeautifulSoup


problem_url = "https://atcoder.jp/contests/abc085/tasks/abc085_a"
problem_html = requests.get(problem_url)
problem_soup = BeautifulSoup(problem_html.content, "html.parser")
for i in problem_soup.find_all("pre"):
    print(i.get_text())
