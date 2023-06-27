# DisFeed
Send RSS feeds changes (monitor) to Discord using webhooks and cronjobs / services!

# How to use
Make sure you have Python, requests and feedparser installed!
<br>
To install, either use crontab or a service
<br>
<br>
Cronjob:
<br>
Edit your crontab and for every feed, after the time, add: 
<br>
```/usr/bin/python3 (path for feed.py) (rss link) (webhook link) (path for file name for the time of last article to be stored)```
<br>
You can use [Crontab Guru](https://crontab.guru) for cronjob stuff.
<br>
<br>
Service:
<br>
Edit ```/etc/systemd/system/Disfeed.service```
<br>
And complete the file with this, configuring it:
```
[Unit]
Description=disfeed
Requires=network.target
After=network.target

[Service]
WorkingDirectory=/home/<username>
User=<username>
Group=<username>
Type=simple
ExecStart=/usr/bin/python3 (path for feed.py) (rss link) (webhook link) (path for file name for the time of last article to be stored)
Restart=always
RestartSec=time between checks

[Install]
WantedBy=multi-user.target
```


# Example line
```*/15 * * * * /usr/bin/python3 /home/ubuntu/feed.py https://example.com/index.xml https://discordapp.com/1235134123/asdadguygHAYUAHSD/ examplecom.txt```

# Other stuff
If many new articles have been added in time between checks, the script might not be able to send all messages due to the rate limit from Discord. Make sure your path to the script and to the Python is correct for your distro and available to all users.
<br>
<br>
<br>
And that's all!
