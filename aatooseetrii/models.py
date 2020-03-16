from django.db import models


class CatTable(models.Model):
    kfactname = models.CharField(max_length=24, blank=True)
    kcatfact = models.TextField()

    def __str__(self):
        return self.kfactname


class GreatWordsTable(models.Model):
    gwordsstater = models.CharField(max_length=32, blank=True)
    gwords = models.TextField()

    def __str__(self):
        return self.gwordsstater


class NatPark(models.Model):
    ntitle = models.CharField(max_length=200)
    ndescription = models.TextField()
    npicture = models.ImageField(blank=True)
    nlocation = models.URLField(blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.ntitle


class Seuraaja(models.Model):
    smaili = models.EmailField()
    skutsumanimi = models.CharField(max_length=32, blank=True)
    saika = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.smaili
