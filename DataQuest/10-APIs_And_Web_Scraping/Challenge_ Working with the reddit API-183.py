## 2. Authenticating with the API ##

headers = {"Authorization":"bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk",
          "User-Agent":"Dataquest/1.0"}
parameter = {"t":"day"}

response = requests.get("https://oauth.reddit.com/r/python/top",headers=headers,params=parameter)
python_top = response.json()



## 3. Getting the Most Upvoted Post ##

print(python_top["data"]["children"][0]["data"]["ups"])

most_upvoted_ups = 0
most_upvoted = 0
for each in python_top["data"]["children"]:
    if each["data"]["ups"] > most_upvoted_ups:
        most_upvoted_ups = each["data"]["ups"]
        most_upvoted = each["data"]["id"]

print("Most Upvoted UP count = {}\tMost Upvoted ID = {}".format(most_upvoted_ups,most_upvoted))

## 4. Getting Post Comments ##

base_url = "https://oauth.reddit.com"
subreddit = "python"
article_id = most_upvoted

url = base_url+"/r/"+subreddit+"/comments/"+article_id
print(url)

response = requests.get(url,headers=headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]

most_upvoted_comment = 0
most_upvoted_comment_ups = 0
for each in comments_list["data"]["children"]:
    if each["data"]["ups"] > most_upvoted_comment_ups:
        most_upvoted_comment_ups = each["data"]["ups"]
        most_upvoted_comment = each["data"]["id"]
        
print("Most Upvoted Comment = {}\nUpvotes = {}".format(most_upvoted_comment,most_upvoted_comment_ups))

## 6. Upvoting a Comment ##

payload = {"dir":1, "id":"d16y4ry"}
status = requests.post("https://oauth.reddit.com/api/vote",headers=headers,json=payload).status_code