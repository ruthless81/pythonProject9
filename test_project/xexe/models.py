from django.db import models

class Event(models.Model):
    date = models.DateField()
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.user} - {self.description}"