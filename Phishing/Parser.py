from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("開始タグは", tag,"です。付属されている属性は",attrs,"です")

    def handle_endtag(self, tag):
        print("終了タグは", tag,"です")

parseTag = MyParser()
parseTag.feed('<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="css/test.css"><title>test</title></head>')