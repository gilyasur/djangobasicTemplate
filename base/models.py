from django.db import models

class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=20)
    price = models.FloatField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.description
