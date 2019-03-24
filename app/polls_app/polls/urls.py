from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path(
        '',
        views.IndexView.as_view(), 
        name='index'
    ),
    # path('', views.index, name='index'),

    # ex: /polls/5/
    path('<int:pk>/', views.PollsDetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    path(
        '<int:pk>/results/',
        views.PollsResultsView.as_view(),
        name='results'
    ),

    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),


    # path('questions', views.IndexViewQuestion.as_view(), name='questions')
    # path('questions/', views.IndexViewQuestion.as_view())
]
