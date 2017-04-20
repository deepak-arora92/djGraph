from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.core import serializers
from models import *
import json


def index(request):
    return HttpResponse("Hello World")

def getNodes(request):
	n = Node.objects.all()
	e = Edge.objects.all()
	nodes = serializers.serialize('json',n)
	edges = serializers.serialize('json',e)
	context = {'nodes':nodes,'edges':edges}
	return render(request, 'graph.html',context)