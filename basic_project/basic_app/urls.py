from django.conf.urls import url,include
from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('page1/$',views.page1,name='page1'),
    path('page2/$',views.page2,name='page2'),
    path('',views.index,name='index'),
]
