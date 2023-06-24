# DisFeed
Send RSS feeds to Discord using webhooks and cronjobs!

# How to use
Make sure you have Python, requests and feedparser installed!
Edit your crontab and for every feed, after the time, add: 
<br>
```/usr/bin/python3 (path for feed.py) (rss link) (webhook link) (path for file name for the time of last article to be stored)```
<br>
You can use [Crontab Guru](https://crontab.guru) for cronjob stuff.
<br>

# Example line
```*/15 * * * * /usr/bin/python3 /home/ubuntu/feed.py https://example.com/index.xml https://discordapp.com/1235134123/asdadguygHAYUAHSD/ examplecom.txt```

# Other stuff
If many new articles have been added in time between checks, the script might not be able to send all messages due to the rate limit from Discord. Make sure your path to the script and to the Python is correct for your distro and available to all users.
<br>
<br>
<br>
And that's all!
