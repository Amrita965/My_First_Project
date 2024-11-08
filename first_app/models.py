from django.db import models

# Create your models here.
class Musician(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50) # blank = True, null = True
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"First Name: {self.first_name} Last Name: {self.last_name}"


class Album(models.Model):
    # id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Musician, on_delete=models.RESTRICT)
    name = models.CharField(max_length = 100)
    release_date = models.DateField()
    ratings = (
        (1, "Worst"),
        (1, "Bad"),
        (1, "Not Bad"),
        (1, "Good"),
        (1, "Excellent!"),
    )
    num_starts = models.IntegerField(choices=ratings)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + str(self.num_starts)