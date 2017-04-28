# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
DISEASE_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
# Create your models here.
class PhenoDb(models.Model):
	id = models.AutoField(primary_key=True)
	gene = models.CharField(max_length=20)
	disease = models.CharField(max_length=150)