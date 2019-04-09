from rest_framework import serializers
from .models import Bucketlist, Tag, Member, PostActivity, Todo
class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id','name', 'title')

class PostActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostActivity
        fields = ('members','status')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','description','due_date','status','date_created','date_modified','tag_list','member_list')
        read_only_fields = ('date_created', 'date_modified')