from django.urls import path


from noticias import views


urlpatterns = [
    path('', views.HomeView.as_view()),
]
