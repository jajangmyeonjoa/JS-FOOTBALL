from django.db import models

# Create your models here.

class Match(models.Model):
    match_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.match_title
    
class Choice(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    choice_team = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_team

"""class graph:
    def __init__(self, first_data, second_data):
        width = 300
        first_ratio = first_data / (first_data + second_data)
        second_ratio = second_data / (first_data + second_data)
        self.firstbar_xcoor = (width*first_ratio-width)/2
        self.secondbar_xcoor = (width*second_ratio-width)/2
        self.firstbar_width = first_ratio*width
        self.secondbar_width = second_ratio*width"""
