# Newsroom, a Django powered news app
Newsroom is a simple Django app that converts markdown syntax into news articles.

![screenshot][https://raw.githubusercontent.com/OulipianSummer/newsroom/master/newsroom_screenshot.png]


## Django Playground
This project was started to act as a sort of sandbox for employing some of Django's more advanced features like custom template tags, context processors, fixtures, and queryset filtering.

**Here are some of the more exciting features of this app.**

| Django Feature | Use In This App |
|-----------------| --------------
| Markdown Conversion | Articles are converted from Markdown to HTML for use a in each article. |
| Template Tags | A set of custom template tags convert strip markdown syntax from each article an generate a short 150 character lead for the article's list views. |
| Context Processors | A custom context processor provides Django Model information to the layout.html template. |
| Fixtures | For testing purposes, a set of fake articles can be called using the `loaddata` command, but more articles could be imported using AJAX and some JSON processing. |

## How to use

**Pre-Setup Note**
This Django project has had the secret key removed, just in case I decide to deploy it someday. In the mean time, you will need to make your own secret key and add it to the /django_news/settings.py file.

If you need help with this step, [here is a handy guide on making a new secret key](https://humberto.io/blog/tldr-generate-django-secret-key/).

1. First, install the requirements for this app (Django 3.1, BeautifulSoup 4, Markdown 3.3)

```
pip3 install -r requirements.txt
```

2. Next, run apply the default migrations

```
python manage.py makemigrations
python manage.py migrate
```

3. Optionally, you can load a set of fake articles and authors from the built in fixtures

```
python manage.py loaddata articles.json authors.json sections.json
```

4. As another optional step, you can create a super user account for yourself so you can check out Django's admin suite and add your own articles

```
python manage.py createsuperuser
```

4. Finally, you can run the test server using the standard Django server command

```
python manage.py runserver
```

With any luck, everything will be up and running!
