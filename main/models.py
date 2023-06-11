from django.db import models

class Repo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # name of repo in <creator>/<repo_name> format
    name = models.CharField(max_length = 200, unique=True)

    forks_count = models.IntegerField(default=0, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length = 400, blank=True, null=True)

    def __str__(self):
        return self.name 

class Contributor(models.Model):
    repos = models.ManyToManyField(Repo)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    github_login = models.CharField(max_length = 39, unique=True)
    github_created_at = models.CharField(max_length = 100, unique=True)

    name = models.CharField(max_length = 500, blank=True, null=True)
    email = models.EmailField(max_length = 254, blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    hireable = models.BooleanField(blank=True, null=True)
    twitter_username = models.CharField(max_length=15, blank=True, null=True)
    avatar_url = models.URLField(max_length = 400, blank=True, null=True)
    blog =  models.URLField(max_length = 400, blank=True, null=True)
    bio = models.CharField(max_length=160, blank=True, null=True)
    company = models.CharField(max_length = 100, blank=True, null=True)
    location = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.github_login 