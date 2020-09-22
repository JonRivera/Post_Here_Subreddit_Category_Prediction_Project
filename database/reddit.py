"""Leverages the reddit api + queries.py to get reddit posts and upload them to a postgres database"""
import praw
import psycopg2

from database.query import insert_post, conn_curs

with open("secrets", "r") as file:
    secrets = [i.strip('\n') for i in file.readlines()]
reddit = praw.Reddit(client_id=secrets[0],
                     client_secret=secrets[1],
                     username=secrets[2],
                     password=secrets[3],
                     user_agent=f'u/{secrets[1]}')

# Accessing Allans Data Base
with open("secrets2", "r") as file:
    secrets2 = [i.strip('\n') for i in file.readlines()]


def conn_curs2():
    """
    makes a connection to the database dont worry these are dummy keys
    """
    connection = psycopg2.connect(dbname=secrets2[4], user=secrets2[4],
                                  password=secrets2[5], host=secrets2[6])
    cursor = connection.cursor()
    return connection, cursor


conn2, curs2 = conn_curs2()
curs2.execute("SELECT Distinct(subreddit) FROM posts")
Subreddits = [i[0] for i in curs2.fetchall()]


def get_data(subs, n_posts=1):
    """
    Fetches then upload a post to postgres

    subs - set of sub-reddits you plan to get posts from
    n_posts - how many posts to grab per sub
    """
    conn, curs = conn_curs()
    curs.execute("SELECT Distinct(subreddit) FROM posts")
    x = [i[0] for i in curs.fetchall()]
    for i in subs:
        if i not in x:
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
    reddits = {'whatsthatbook', 'CasualConversation', 'Clairvoyantreadings',
               'DecidingToBeBetter', 'HelpMeFind', 'LifeProTips', 'MLPLounge',
               'NoStupidQuestions', 'RBI', 'TooAfraidToAsk', 'answers', 'ask',
               'changemyview', 'christmas', 'explainlikeimfive', 'findapath',
               'getting_over_it', 'help', 'ifyoulikeblank', 'makemychoice',
               'needadvice', 'selfhelp', 'selfimprovement', 'tipofmytongue',
               'whatisthisthing', 'theydidthemath', 'datarecovery', 'declutter',
               'GetMotivated', 'getdisciplined', 'productivity', 'GiftIdeas',
               'Gifts', 'IWantOut', 'ImmigrationCanada', 'immigration', 'ukvisa',
               'nosurf', 'AusLegal', 'LegalAdviceUK', 'asklaw', 'legal',
               'legaladvice', 'legaladviceofftopic', 'INeedAName',
               'whatsthisplant', 'resumes', 'NameThatSong', 'StopGaming',
               'translator', 'whatsthisworth', 'whatstheword', 'WouldYouRather',
               'Beekeeping', 'bettafish', 'Pets', 'reptiles', 'AquaSwap',
               'CatAdvice', 'cats', 'BackYardChickens', 'Petloss', 'Dogtraining',
               'dogs', 'puppy101', 'ferrets', 'guineapigs', 'hamsters', 'Bedbugs',
               'whatsthisbug', 'leopardgeckos', 'BeardedDragons', 'parrots',
               'pestcontrol', 'Rabbits', 'RATS', 'shrimptank', 'ballpython',
               'snakes', 'tarantulas', 'ShingekiNoKyojin', 'Berserk', 'bleach',
               'BokuNoHeroAcademia', 'Animesuggest', 'anime', 'manga',
               'CaptainTsubasaDT', 'DarlingInTheFranxx', 'deathnote', 'DDLC',
               'Dragonballsuper', 'dbz', 'fatestaynight', 'Gundam', 'Gunpla',
               'HunterXHunter', 'StardustCrusaders', 'KissAnime', 'araragi'}
    get_data(reddits, n_posts=300)