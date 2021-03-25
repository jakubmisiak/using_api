from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30, null=False)

    def get_absolute_url(self):
        return f"/{self.id}"