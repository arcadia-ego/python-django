from rest_framework import serializers, viewsets
from .models import Bookmark

class Bookmark_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Bookmark
	    fields = ('title', 'url')
    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        newBookmark = Bookmark.objects.create(user=user, **validated_data)
        return newBookmark

class Bookmark_Viewset(viewsets.ModelViewSet):
    serializer_class = Bookmark_Serializer
    queryset = Bookmark.objects.none()
    def get_queryset(self):
        # queryset = Bookmark.objects.none()
        user = self.request.user
        if user.is_anonymous:
            return Bookmark.objects.none()
        else:
            return Bookmark.objects.filter(user=user)
