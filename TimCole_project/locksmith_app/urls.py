from django.conf.urls import url
from locksmith_app import views

app_name = 'locksmith_app'

urlpatterns = [
    url(r'^$',views.home,name ='home'),
    url(r'^about/$',views.about,name = 'about'),
    url(r'^contact/$',views.contact,name = 'contact'),
    url(r'^services/$',views.services,name = 'services'),
    ]
