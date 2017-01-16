from django.conf.urls import url

from . import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='homepage'),
    url(r'^category/$', views.HomepageView.as_view(), name='category'),
]