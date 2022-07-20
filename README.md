# Gday, mate!

[![Deploy master](https://github.com/nikilyushkin/gday/actions/workflows/deploy.yml/badge.svg)](https://github.com/nikilyushkin/gday/actions/workflows/deploy.yml)

Gday.mate is a small web service that shows multiple RSS sources on one page and performs tricky parsing and summarizing articles using TextRank algorithm. 

It helps to keep track of news from different areas without subscribing to hundreds of media accounts and getting annoying notifications.

Thematic and people-based collections does a really good job for discovery of new sources of information. Since we all are biased, such compilations can really help us to get out of information bubbles.

The code of the service created by [Vas3k.club](https://vas3k.club) community. The original service is live [here](https://infomate.club).

### Live URL: [gday.iocats.com](https://gday.iocats.com)

![](https://previews.dropbox.com/p/thumb/ABkX6Alcbfjc5v76Eg0BfZoOyCwZgUlJrGQwFklDpucTFCLoeIoiG0-5P1J7P6UfkbKbQEKMqM3zLy2Nlttmwcigqn6SXCKkhMeZYRvq5cUeHu1ki2V83k8xcXrB9YoxUz43FgPfonzTltyRlDI-NY4rlWJZ-IUx1qJte88CuFXz0iiu6yiGTfiG44Szq9M_uVEZ9lgjf4VbMuoXI9OH7XFUwUO9S-2KfwulaJ5KKS6gSMIqKd9DSrmZ3t6dRVXPlXmfdhpEWHfQQ6gO6lf0hpku7JiTsJ_G2HbNxl8A3ukN_jW9Ry1vscs-frzk-tGeoYsQD856zncsENmVtdL1QTPKQqKjuCSQYiQTKe7n_Q3eJCrx8Ak-REUlqADzufuGswI/p.png)

## 🐶 This is a for of a pet-project

Which means you really shouldn't expect much from it.  No state-of-art kubernetes bullshit, no architecture patterns, even no tests at all. It's here just to show people what a pet-project might look like.

This code has been written for fun, not for business. 

## 🤔 How it works

It's basically a Django web app with a bunch of [scripts](scripts) for RSS parsing. It stores the parsed data in a PostgreSQL database.

The web app is only used to show the data (with heavy caching). 
Parsing and feed updates are performed by the three scripts running in cron. Like poor people do.

[Feedparser](https://pythonhosted.org/feedparser/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) are used to find, download and parse RSS. 

Text summarization is done via [newspaper3k](https://newspaper.readthedocs.io/en/latest/) with some additional protection against bad types of content like podcasts and too big pages in general, which can eat all your memory.

## ▶️ Running it locally

The easy way. Install [docker](https://docs.docker.com/install/) on your machine. Then:

```
git clone git@github.com:nikilyushkin/gday.git
cd gday
docker-compose up --build
```

On the first run you might need to wait until the "migrate_and_init" container will finish its job populating your database. 

It takes a while.

After that you can open [localhost:8000](http://localhost:8000) in your favorite browser and enjoy.

If something stucked or you want to terminate it completely, use this command in another terminal:

```shell script
docker-compose down --remove-orphans
```


## ⚙️ boards.yml format

All collections and feeds are stored in one file — [boards.yml](boards.yml). 
This is your main and only entry point to add new stuff. 

```
boards:
- name: Tech            # board title
  slug: tech            # board url
  is_visible: true      # visibility on the main page
  is_private: false     # private boards require logging in
  curator:              # board author profile
    name: John Wick 
    title: Main news
    avatar: https://i.vas3k.ru/fhr.png 
    bio: Major technology media in English and Russian
    footer: >
      this is a general selection of popular technology media.
      The page is updated once per hour.
  blocks:               # list of logical feed blocks
  - name: English       # block title
    slug: en            # unique board id
    feeds:         
      - name: Hacker News
        url: https://news.ycombinator.com
        rss: https://news.ycombinator.com/rss
      - name: dev.to
        url: https://dev.to
        rss: https://dev.to/feed
      - name: TechCrunch
        rss: http://feeds.feedburner.com/TechCrunch/
        url: https://techcrunch.com
        is_parsable: false  # do not try to parse pages, show RSS content only
        conditions:
          - type: not_in
            field: title
            word: Trump   # exclude articles with a word "Trump" in title
```

## 💎 Running in production

Deployment is done using a simple Github Action which builds a docker container, puts it into Github Registry, logs into your server via SSH and pulls it. 
The pipeline is triggered on every push to master branch. If you want to set up your own fork, please add these constants to your repo SECRETS:

```
APP_HOST — e.g. "https://your.host.com"
GHCR_TOKEN — your personal guthib access token with permissions to read/write into Github Registry
SECRET_KEY — random string for django stuff (not really used)
SENTRY_DSN — if you want to use Sentry
PRODUCTION_SSH_HOST — hostname or IP of your server
PRODUCTION_SSH_USERNAME — user which can deploy to your server
PRODUCTION_SSH_KEY — private key for this user
```

After you install them all and commit something to the master, the action should run and deploy it to your server on port **8816**. 

Don't forget to set up nginx as a proxy for that app (add SSL and everything else in there). Here's example config for that: [etc/nginx/infomate.club.conf](etc/nginx/infomate.club.conf)

If something doesn't work, check the action itself: [.github/workflows/deploy.yml](.github/workflows/deploy.yml)

## 🎉 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

You can help us with opened issues too. There's always something to work on.

We don't have any strict rules on formatting, just explain your motivation and the changes you've made to the PR description so that others understand what's going on.

## 👩‍💼 License

[Apache 2.0](LICENSE) © Vasily Zubarev

> TL;DR: you can modify, distribute and use it commercially, 
but you MUST reference the original author or give a link to service