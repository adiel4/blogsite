from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.indexpage, name="index"),
    path("home", views.indexpage, name="index"),
    path("home/", views.indexpage, name="index"),
    path("about", views.aboutpage, name='about'),
    path("about/", views.aboutpage, name='about'),
    path('contact', views.contactpage, name='contact'),
    path('contact/', views.contactpage, name='contact'),
    path('article/<int:article_id>', views.articlepage, name="article"),
    path('article/<int:article_id>/', views.articlepage, name="article"),
    path('postcomment/<int:article_id>', views.commentpost, name='postcomment')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
