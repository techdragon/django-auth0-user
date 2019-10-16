from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='test_app/example.html'), name='home'),
]
