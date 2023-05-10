from operator import itemgetter
import requests

#make API call and store the response
url ='htps://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Process info about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:3]:
    #make a seperate API call for each submission
    url1 =f"https:/hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r1 = requests.get(url1)
    print(f"id: {submission_id}\tstatus: {r1.status_code}")
    response_dict: r1.json()

    #Build a dictionary for each article
    submission_dict ={
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
#itemgetter - sorts based on the key you want to sort by

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['commets']}")