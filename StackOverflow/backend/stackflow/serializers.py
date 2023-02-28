from rest_framework import serializers
from .models import User, Question, Answer,Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Answer
        fields = ['id', 'body', 'user', 'created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# this is the serializer that is handling the post request of a question getting posted by the user     
class QuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'user', 'upvotes', 'downvotes', 'created_at', 'updated_at', 'num_answers','num_comments', 'tags']
    
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        if not tags_data:
            raise serializers.ValidationError('At least one tag is required.')
        tags = [Tag.objects.get_or_create(**tag_data)[0] for tag_data in tags_data]
        question = Question.objects.create(**validated_data)
        question.tags.set(tags)
        return question

