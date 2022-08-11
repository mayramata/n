
from django.urls import  path, include
from profilesapi import views
#para viewset 
from rest_framework.routers import DefaultRouter


#viewset
router = DefaultRouter()
router.register("welcometo-viewset", views.WelcomeToViewSet, basename="welcometo-viewset")
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserProfileFeedViewSet)

#viewapi
urlpatterns = [
    path("welcome-view/", views.WelcomeToTheApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("",include(router.urls))
]