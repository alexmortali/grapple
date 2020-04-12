from django.conf.urls import url
from .views import payment, review

app_name = 'checkout'

urlpatterns = [
    url(r'^$', review, name='review'),
    url(r'^payment/$', payment, name='payment'),
]
