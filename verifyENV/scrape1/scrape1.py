import requests
from bs4 import BeautifulSoup


problem_url = "https://atcoder.jp/contests/abc081/tasks/abc081_a"
problem_html = requests.get(problem_url)
problem_soap = BeautifulSoup(problem_html.content, "html.parser")
print(problem_soap)
