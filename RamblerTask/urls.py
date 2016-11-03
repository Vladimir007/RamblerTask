from django.conf.urls import url
from django.contrib import admin
from RamblerTask import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_page, name='error'),
    url(r'^calc_pickle/$', views.calculate_pickle),
    url(r'^change_pickle/$', views.change_pickle)
]
