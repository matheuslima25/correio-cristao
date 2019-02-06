from django.urls import path


from noticias import views


urlpatterns = [
    path('', views.HomeView.as_view()),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/<slug:slug>/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('video/<int:pk>', views.VideoDetailView.as_view(), name='video_detail'),
    path('sobre/', views.AboutView.as_view(), name='about'),
    path('comercial/', views.AdsView.as_view(), name='comercial'),
    path('contato/', views.contact, name='contact'),
    path('sucesso/', views.SuccessView.as_view(), name='success'),
    path('pesquisar/', views.pesquisar, name='search'),
    path('privacidade/', views.PrivacyView.as_view(), name='privacidade'),
    path('lista/video/', views.VideoView.as_view(), name='video_list'),
    path('lista/<slug:slug>/', views.CategoryView.as_view(), name='category_list'),
]
