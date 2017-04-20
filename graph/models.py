from __future__ import unicode_literals

from django.db import models

# Create your models here.

	
class Node(models.Model):
    node_id = models.AutoField(primary_key = True)
    node_name = models.CharField(max_length=200)
    node_data = models.CharField(max_length=200)

class Edge(models.Model):
	edge_id = models.AutoField(primary_key = True)
	from_id = models.ForeignKey(Node, on_delete=models.CASCADE, related_name = 'from_id')
	to_id = models.ForeignKey(Node, on_delete=models.CASCADE, related_name = 'to_id')
	weight = models.IntegerField(default=None)