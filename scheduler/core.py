import schedule
import praw


def post(user, subreddit, title, text, url):
    if text and url:
        print('You can not post text and URL at once!')
        return

    reddit = user.reddit()
    sr = reddit.subreddit(subreddit)
    submission = sr.submit(title=title, selftext=text, url=url)
    submission.upvote()
    return submission.shortlink
