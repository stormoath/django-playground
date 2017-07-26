from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    COLORS = (
        ('A1D490','green'),
        ('90C3D4','blue'),
        ('D4A190','red'),
        ('EAFF96','yellow'),
        ('FFFFFF','white'),
    )
    color = models.CharField(max_length=7, choices=COLORS)
    pubdate = models.DateTimeField('date published')

    def __str__(self):
        return self.title
