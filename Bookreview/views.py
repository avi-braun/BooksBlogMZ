from django.shortcuts import render
from django.http import HttpResponse
from mezzanine.pages.models import Page
from django.db import models
from .models import myReview

from mezzanine.blog.models import BlogPost

# #
# class Author(Page):
#     dob = models
#     print (dob)

# for users in models.DateField:
#     print(users)

def index(request):
    # latest_reviews = BlogPost.objects.order_by('-pub_date')[:5]
    reviews=BlogPost.publish_date
    reviews2=myReview.user
    # reviews='4'
    context = {'review_urls': reviews2}
    return render(request, 'Bookreview/index.html', context)


def gallery(request):
    return HttpResponse("Gallery")