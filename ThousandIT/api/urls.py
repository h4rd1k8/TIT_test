from django.urls import path
from api import views

urlpatterns = [
    path('rubrics/', views.RubricList.as_view()),
    path('rubrics/<int:pk1>/', views.RubricList.as_view()),
    path('rubrics/<int:pk1>/news', views.NewsList.as_view()),
    path('rubrics/<int:pk1>/news/<int:pk2>/', views.News.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout', views.logout),
]
