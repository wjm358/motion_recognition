
from django.conf.urls import url
from django.contrib import admin

from emotion import views as emotion_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout_process',emotion_views.logout_process, name='logout_process'),
     url(r'^moviemain/', emotion_views.moviemain, name='moviemain'),
    url(r'^$',emotion_views.HomeView.as_view(),name='home'),
    url(r'^check_login/',emotion_views.check_login, name='check_login'),
    url(r'^user_registration/',emotion_views.user_registration, name='user_registration' ),
    url(r'^password/$', emotion_views.change_password, name='change_password'),
    url(r'^list_video/',emotion_views.list_video,name='list_video'),
    url(r'^search_video/',emotion_views.search_video,name='search_video'),

]
