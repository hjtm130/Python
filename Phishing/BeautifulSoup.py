from bs4 import BeautifulSoup
html_list = '    <body><h2>タイトル</h2><p>テスト</p></body>'
html_parse = BeautifulSoup(html_list, 'html.parser')
print('h2: ', html_parse.h2.string)
print('p: ', html_parse.body.p.string)