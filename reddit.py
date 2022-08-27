import requests
import sys #ask for abstract methods
import os
import pandas as pd
from PIL import Image
import re
from subreddit_query import subreddit_query


class RedditPost:
    def __init__(self, data):
         #assuming that data will come as in this format data['data']['children'][i] so I can iterate over to create RedditPost objects
        required_keywords = ["subreddit","is_self","ups","post_hint","title","downs", \
            "score","url","domain","permalink","created_utc","num_comments","name","over_18"]
        self.data = data['data']
        self.required_data = {key:value for (key,value) in self.data.items() if key in required_keywords}
        
    
    def __str__(self):
        title = self.required_data['title']
        score = self.required_data['score']
        url = self.required_data['url']
        return f"RedditPost -> title : {title}, score : {score}, url : {url}"
    
    def download(self):
        
        if self.is_downloadable() == True:
            print("Give it a minute -- It is downloading")
            todownload = requests.get(self.required_data['url'],allow_redirects = True)
            
            with open("wallpapers/" + self.name_image() + ".png", 'wb') as file:
            
                file.write(todownload.content)
                print("One image downloaded.")
            return f"It is downloaded"
        
        else:
            print("Download failed")
            
            return f"download fail"
    
    def is_downloadable(self):
        url = self.required_data['url']
        header = requests.head(url,allow_redirects=True)
        if 'Content-Type' in header.headers:
            content_type = header.headers.get('Content-Type')
            if "image" in content_type:
                return True
            else:
                return False
            
        return False
    
    def name_image(self):
        
        pattern = re.compile(r'''
            (
                [\[\(]? \d+ [x×] \d+ [\]\)]?  # like [1920×1080], 1x0, (1x0)
                | \[.*\]  # notes like [not OC]
                | [;/"+]    # other chars
                | [^0-9a-zA-Z" "]+ #otherchars
            )
                        ''', re.VERBOSE)
        
        image_title = pattern.sub('', self.required_data['title'])[:40].strip()
        
        return image_title

def get_urls(reddit_posts):
    return [post.required_data['url'] for post in reddit_posts if post.is_downloadable() == True]

def main():
    params = None
    urls = []
    for _ in range(2):
        json_data = subreddit_query('wallpaper',params)
        reddit_posts = [RedditPost(child) for child in json_data['data']['children']]

        urls.append(get_urls(reddit_posts)) #gets urls for our streamlit app
        
        
    
        for post in reddit_posts:
             #post.download()
             print(post)
             print("------------")
            
        next_page = json_data['data']['after']
        params = dict(after=next_page)

    return urls

if __name__ == "__main__":
    main()
