"""Leverages the reddit api + queries.py to get reddit posts and upload them to a postgres database"""
import praw
from database.query import insert_post

with open("secrets", "r") as file:
    secrets = [i.strip('\n') for i in file.readlines()]
reddit = praw.Reddit(client_id=secrets[0],
                     client_secret=secrets[1],
                     username=secrets[2],
                     password=secrets[3],
                     user_agent=f'u/{secrets[1]}')


def get_data(subs, n_posts=1):
    """
    Fetches then upload a post to postgres

    subs - set of sub-reddits you plan to get posts from
    n_posts - how many posts to grab per sub
    """
    for i in subs:
        sub = reddit.subreddit(i)
        hot = sub.hot(limit=n_posts)
        for post in hot:
            text = f"{post.title} {post.selftext}".replace("'", "")
            which_sub = str(post.subreddit)[:20]
            insert_post(text, which_sub)
            print('uploaded')
        print('Finished sub')
    return


if __name__ == "__main__":
    reddits = {'learnSQL', 'MovieSuggestions', 'dating_advice', 'philosophy', 'worldnews', 'tifu', 'patientgamers',
               'explainlikeimfive', 'OutOfTheLoop', 'books', 'ProRevenge', 'TellMeAFact', 'bestoflegaladvice',
               'talesfromtechsupport', 'TalesFromRetail', 'britishproblems', 'whowouldwin', 'WritingPrompts', 'AskMen',
               'AskWomen', 'askscience', 'newreddits', 'HailCorporate', 'boringdystopia', 'bestof', 'KarmaCourt',
               'AmItheAsshole', 'RedditWritesSeinfeld', 'Nosleep', 'pcmasterrace', 'learnpython'}

    get_data(reddits, n_posts=300)

# need a conditional in the outer loop to check if sub in db,
# make conn excute distinct query fetchall then if not in x
# if not i in curs.execute("SELECT Distinct(subreddit)")[0][0]: