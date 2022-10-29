from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

# Create your views here.
@api_view(['GET'])
def index(request):

    return Response({"slackUsername": "Jojothomas", "backend": True, "age": 24, "bio": "I LOVE TO BUILD AND TWEAK THINGS" });