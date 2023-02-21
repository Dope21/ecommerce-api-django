from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
  person = {
    "name": "someone", 
    'age': 25
  }
  return Response(person)
