from rest_framework import serializers
from .models import User, Question, Answer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Answer
        fields = ['id', 'body', 'user', 'created_at', 'updated_at']



# this is the serializer that is handling the post request of a question getting posted by the user     
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'user', 'upvotes', 'downvotes', 
                  'created_at', 'updated_at', 'num_answers','num_comments', 'tags']

