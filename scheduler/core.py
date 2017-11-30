import celery


@celery.task(ignore_result=True)
def post(user, post):
    if post.text and post.url:
        print('You can not post text and URL at once!')
        return

    reddit = user.reddit()
    sr = reddit.subreddit(post.subreddit)
    submission = sr.submit(title=post.title, selftext=post.text, url=post.url)
    submission.upvote()
    post.posted = True
    post.save()
    return submission.shortlink
