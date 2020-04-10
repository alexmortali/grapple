from django.conf.urls import url
from . import views
app_name = 'reviews'

urlpatterns = [
    url(r'^add_review/$', views.add_review, name='add_review'),
]