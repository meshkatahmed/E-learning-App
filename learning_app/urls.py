from django.urls import path
from . import views


app_name = 'learning_app'

urlpatterns = [
    path('articles/',views.Articles.as_view(),name='articles'),
    path('writearticle/',views.write_article,name='writearticle'),
    path('articledetail/<slug>/',views.ArticleDetail.as_view(),name='articledetail'),
]
