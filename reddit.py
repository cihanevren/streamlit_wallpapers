import requests
import sys #ask for abstract methods
import os
import pandas as pd
from PIL import Image
import re



def subreddit_query(key,params=None):
    
    url = "https://www.reddit.com/r/" + key 
    
    url_json = "https://www.reddit.com/r/" + key + "/.json"
    
    try : 
        
        r = requests.get(url,params = params,headers={'User-Agent': 'Wallscraper Script by @psarin'})
        r.raise_for_status()
        r.ok
        
    except requests.exceptions.HTTPError as e:
        print("Aaaa Page not found! Try another subreddit")
        print(str(e))
        return r
    try:
        response = requests.get(url_json,params = params,headers={'User-Agent': 'Wallscraper Script by @psarin'})
        response.raise_for_status()
    except requests.exceptions.ConnectionError as e:
        print("There is a Connection Error happening around. Just Letting you know")
        print(str(e))

    except requests.exceptions.Timeout as e:
        print("There is a Timeout Error happening around. Just Letting you know")
        print(str(e))

    except requests.exceptions.RequestException as e:
        print("There is a RequestException Error happening around. Just Letting you know")
        print(str(e))

    except KeyboardInterrupt as e:
        print("Well apparently someone intervened the program ")
        print(str(e))
    
    
    return response.json()



class RedditPost:
    def __init__(self,data): #assuming that data will come as in this format data['data']['children'][i] so I can iterate over to create RedditPost objects
        rlvnt = ["subreddit","is_self","ups","post_hint","title","downs","score","url","domain","permalink","created_utc","num_comments","name","over_18"]
        

        self.data = data['data']
        
        self.rlvnt_data = {key:value for (key,value) in self.data.items() if key in rlvnt}
        
        
    
    def __str__(self):
        
        return f"RedditPost -> title : {self.rlvnt_data['title']}, score : {self.rlvnt_data['score']}, url : {self.rlvnt_data['url']}"
    
    def download(self):
        
        if self.is_downloadable() == True:
            print("Give it a minute -- It is downloading")
            todownload = requests.get(self.rlvnt_data['url'],allow_redirects = True)
            
            with open("wallpapers/" + self.name_image() + ".png", 'wb') as file:
            
                file.write(todownload.content)
                print("One image downloaded.")
            return f"It is downloaded"
        
        else:
            print("Download failed")
            
            return f"download fail"
    
    def is_downloadable(self):
        url = self.rlvnt_data['url']
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
        
        image_title = pattern.sub('', self.rlvnt_data['title'])[:40].strip()
        
        return image_title

def get_urls(reddit_posts):
    return [post.rlvnt_data['url'] for post in reddit_posts if post.is_downloadable() == True]

def main():
    params = None
    urls = []
    for _ in range(2):
        json_data = subreddit_query('wallpaper',params)
        reddit_posts = [RedditPost(child) for child in json_data['data']['children']]

        urls.append(get_urls(reddit_posts)) #gets urls for our streamlit app
        
        
    
        # for post in reddit_posts:
        #     post.download()
            
        next_page = json_data['data']['after']
        params = dict(after=next_page)

    return urls

if __name__ == "__main__":
    main()
