# gh-scraping


# Installation

#### clone repo
```
git clone https://github.com/Dolidodzik/gh-scraping.git
cd gh-scraping
```
#### build docker image - this may take a while

```
docker-compose up -d --build
```
#### run migrations and create superuser

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

If you haven't encountered any errors up to this point, and you can login (at localhost:8000/admin) to account you just created, then you are all set.


# Usage

Create new github token (https://github.com/settings/tokens - classic token) and put it into .env, the same way it's done in .env.example
Now to actually get data you need, just use this command (you can replace facebook/react with whatever you want, for example for this repo it would be Dolidodzik/gh-scraping):
```
sudo docker-compose exec web python manage.py scrape --repo_name facebook/react
```
Reading this data and saving it into db can take few up to a few minutes, but it will be there eventually. To check results, go to localhost:8000/admin, and view Contributors and Repos.
