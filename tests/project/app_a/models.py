from django.db import models


class OSMData(models.Model):
    place_id = models.IntegerField()
    osm_data = models.TextField()

    anthem_beginning = models.CharField(max_length=256, null=True)
    first_president = models.CharField(max_length=256)
