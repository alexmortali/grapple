from django.conf.urls import url
from .views import checkout, payment

app_name = 'checkout'

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^payment/$', payment, name='payment'),
]