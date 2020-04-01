from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache



index = never_cache(TemplateView.as_view(template_name='index.html'))
#@api_view(['GET'])
# def index(request):
#     date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     message = 'Server is live, current time is '
#     return Response(data=message + date, status=status.HTTP_200_OK)
