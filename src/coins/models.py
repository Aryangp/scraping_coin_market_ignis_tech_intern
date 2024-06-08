from django.db import models
import uuid

"""
this are all models created for different part of scraped data like jobid and tasks etc 
"""


class Job(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Task(models.Model):
    job = models.ForeignKey(Job, related_name='tasks', on_delete=models.CASCADE)
    coin = models.CharField(max_length=100)

class Output(models.Model):
    task = models.OneToOneField(Task, related_name='output', on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    price_change=models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    market_change=models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    volume_change=models.CharField(max_length=100)
    circulating_supply = models.CharField(max_length=100)
    total_supply = models.CharField(max_length=100)
    diluted_market_cap = models.CharField(max_length=100)

class Contract(models.Model):
    output = models.ForeignKey(Output, related_name='contracts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class OfficialLink(models.Model):
    output = models.ForeignKey(Output, related_name='official_links', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.URLField()

class Social(models.Model):
    output = models.ForeignKey(Output, related_name='socials', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
