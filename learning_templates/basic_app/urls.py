from django.conf.urls import url,include
from basic_app import views

app_name = 'basic-app'

urlpatterns= [
url(r'^relative/$',views.relative,name='relaive'),
url(r'^other/$',views.other,name='other'),
]
