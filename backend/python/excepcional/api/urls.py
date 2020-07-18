from django.urls import path, include, re_path
from rest_framework import routers
from api import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('event/', views.EventList.as_view()),
    re_path(r'event/(?P<pk>\d+)?', views.EventDetail.as_view()),

    path('environment/', views.EnvironmentList.as_view()),
    re_path(r'environment/(?P<pk>\d+)?', views.EnvironmentDetail.as_view()),

    path('application/', views.ApplicationList.as_view()),
    re_path(r'application/(?P<pk>\d+)?', views.ApplicationDetail.as_view()),
    path('application_token/', views.ApplicationToken.as_view()),

    path('user/', views.UserList.as_view()),
    re_path(r'user/(?P<pk>\d+)?', views.UserDetail.as_view()),
    path('user_token/', views.UserToken.as_view()),
]
