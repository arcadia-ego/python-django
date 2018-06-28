from rest_framework import serializers, viewsets
from models.py import Bookmark

class Bookmark_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	model = Bookmark
	fields = (‘title’, ‘url’)

class Bookmark_Viewset(viewsets.ModelViewSet):
    serializer_class = Bookmark_Serializer
    queryset = Bookmark.objects.all()