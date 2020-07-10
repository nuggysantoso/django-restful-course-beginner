from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a List of APIView Features"""
        an_apiview = [
            'Uses HTTP Methods as Function (get,  post, patch, put, delete)',
            'Is similiat to a tradtional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'messages': 'Hello', 'an_apiview': an_apiview})