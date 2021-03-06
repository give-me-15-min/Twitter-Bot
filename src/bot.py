import tweepy
import pprint
from datetime import datetime, timedelta
import key

# Twitterに接続＆認証
auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token_key, key.access_token_secret)
api = tweepy.API(auth)

query = ["to:akakou_py"]

# 検索
for status in api.search(q=query, lang='ja', result_type='recent'):
    print("-*-*-*-*-")
    print(f"name: {status.user.screen_name}\n")    # ユーザ名を表示
    print(f"text: {status.text}\n")         # ツイートの内容を表示
    
    tweet_day = status.created_at + timedelta(hours=9)
    
    today = datetime.today()
    a_hour_ago = today - timedelta(hours=1)
    print(f"time: {tweet_day}\n") # 時間を表示
    
    if tweet_day < a_hour_ago:
        print("message: pass")
        print("-*-*-*-*-\n\n")
        continue

    id = status._json['id']
    print(f"id: {id}\n")
    url = f"https://twitter.com/{status.user.screen_name}/status/{id}"
    print(f"url: {url}")

    print("-*-*-*-*-\n\n")
