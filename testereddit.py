import praw
import sqlite3

# Connect to the Reddit API using PRAW
reddit = praw.Reddit(
    client_id='D-Xwe0RgGdxXdyrIuZgzQA',
    client_secret='vtYpNzEEmXj_8i_L2ing3g1X3ra9tw',
    user_agent='MyRedditApp by /u/gabrielrosa153'
)

# Connect to the SQLite database
conn = sqlite3.connect('reddit_data.db')
c = conn.cursor()

# Create a table to store the Reddit data
c.execute('''CREATE TABLE IF NOT EXISTS reddit_posts
             (id TEXT PRIMARY KEY, title TEXT, body TEXT)''')

# Read random forums from Reddit
subreddits = ['brasil', 'desabafos'] 

for subreddit in subreddits:
    posts = reddit.subreddit(subreddit).random_rising(limit=10)  # Read 10 random rising posts from each subreddit
    
    for post in posts:
        post_id = post.id
        title = post.title
        body = post.selftext
        
        # Save the data in the database
        c.execute("INSERT OR IGNORE INTO reddit_posts VALUES (?, ?, ?)", (post_id, title, body))
        conn.commit()
        
        # Print the post information
        print("Post ID:", post_id)
        print("Title:", title)
        print("Body:", body)
        print("----------------------")

# Close the database connection
conn.close()