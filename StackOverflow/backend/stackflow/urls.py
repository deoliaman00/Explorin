from django.urls import path
from .views import UserList, UserDetail, QuestionList, QuestionDetail, AnswerList, AnswerDetail, TagList, TagDetail,CreateQuestionAPIView

urlpatterns = [
    path('questions/create/',CreateQuestionAPIView.as_view(),name='create-question'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    path('answers/', AnswerList.as_view(), name='answer-list'),
    path('answers/<int:pk>/', AnswerDetail.as_view(), name='answer-detail'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
]
