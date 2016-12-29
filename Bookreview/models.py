from django.db import models
from mezzanine.pages.models import Page
from mezzanine.blog.models import BlogPost

class myPage(Page):
    a=4

class myReview(BlogPost):
    a=4
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
# # Create your models here.
