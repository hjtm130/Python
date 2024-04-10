# ライブラリ「oprnai」の読み込み
import openai
import os

# OpenAIのAPIキーを設定
openai.api_key = os.environ["OPENAI_API_KEY"]

# ChatGPTにリクエストを送信する関数を定義
def make_tweet():
    # ChatGPTに対する命令文を設定
    request = "私は苦手意識からプログラミングを恨む高専生です。私に代わってXに投稿するポストを140字以内で作成してください。\n\nポストを作成する際は、以下の例文を参考にしてください。\n\n"
    # 例文として与える投稿文を設定
    post1 = "例文1：プログラミング嫌い\n\n"
    post2 = "例文2：ChatGPT無理ンゴ\n\n"
    
    # 文章を連結して1つの命令文にする
    content = request + post1 + post2
    
    # ChatGPTにリクエストを送信
    response = openai.Chat