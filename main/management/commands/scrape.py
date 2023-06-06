from django.core.management.base import BaseCommand, CommandError
from github import Github
from main.models import Repo, Contributor
from django.conf import settings


class Command(BaseCommand):
    help = "Scrapes github users from provided link into database"

    def add_arguments(self, parser):
        parser.add_argument('--repo_name')

    def handle(self, *args, **options):
        print("Getting contributors of "+str(options['repo_name'])+"...")

        g = Github(settings.ACCESS_TOKEN)
        print("Connected to github API successfully")

        repo = g.get_repo(options['repo_name'])
        print("Found repo "+repo.html_url+"...")

        print("Adding repo to db...")

        # checking if repo already exists in db
        if Repo.objects.filter(name = options['repo_name']).exists():
            print('This repo was already added before. Data will be refreshed now. If you want to stop refreshing process, you can just ctrl+c at any moment.')
            db_repo = Repo.objects.get(name = options['repo_name'])
            db_repo.forks_count = repo.forks
            db_repo.language = repo.language
            db_repo.html_url = repo.html_url
            db_repo.save()
        else:
            db_repo = Repo(name = options['repo_name'], forks_count = repo.forks, language = repo.language, url = repo.html_url)
            db_repo.save()

        print("Reading contributors and saving them into db...")
        contributors = repo.get_contributors()
        
        count = 0
        for contributor in contributors:
            count += 1
            # checking if contributor already exists in db
            if Contributor.objects.filter(github_login = contributor.login).exists():
                db_contributor = Contributor.objects.get(github_login = contributor.login)

                db_contributor.email = contributor.email
                db_contributor.followers_count = contributor.followers
                db_contributor.hireable = contributor.hireable
                db_contributor.twitter_username = contributor.twitter_username
                db_contributor.avatar_url = contributor.avatar_url
                db_contributor.blog = contributor.blog
                db_contributor.bio = contributor.bio
                db_contributor.company = contributor.company
                db_contributor.location = contributor.location
                db_contributor.save()
            else:
                db_contributor = Contributor(
                    github_login = contributor.login, 
                    email = contributor.email,
                    followers_count = contributor.followers,
                    hireable = contributor.hireable,
                    twitter_username = contributor.twitter_username,
                    avatar_url = contributor.avatar_url,
                    blog = contributor.blog,
                    bio = contributor.bio,
                    company = contributor.company,
                    location = contributor.location,
                    github_created_at = contributor.created_at
                )
                db_contributor.save()

                # adding newly created user to given repo
                db_contributor.repos.add(Repo.objects.get(name = options['repo_name']))

            if count % 100 == 0:
                print("Already "+ str(count) +" contributors processed!")
        
        
        print("Done. "+ str(count) + " contributors were found in this repo.")
    
