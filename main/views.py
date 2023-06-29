from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Contributor


def dump_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['created_at', 'updated_at', 'github_login', 'github_created_at', 'name', 'email', 'email_from_patch', 'followers_count', 'hireable', 'twitter_username', 'avatar_url', 'blog', 'bio', 'company', 'location'])

    contributors = Contributor.objects.all().values_list('created_at', 'updated_at', 'github_login', 'github_created_at', 'name', 'email', 'email_from_patch', 'followers_count', 'hireable', 'twitter_username', 'avatar_url', 'blog', 'bio', 'company', 'location')
    for contributor in contributors:
        writer.writerow(contributor)

    return response
    
