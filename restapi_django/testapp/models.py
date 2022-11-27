from django.db import models


# Create your models here.


class TestClass(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    main_category = models.CharField(max_length=40)
    last_update = models.DateField()

    def __str__(self):
        return self.main_category
