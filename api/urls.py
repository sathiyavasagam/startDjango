from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from rest_framework.decorators import api_view


urlpatterns = {
    url(r'^orders/$', CreateView.as_view(), name="create"),
        url(r'^upload/$' ),

}

urlpatterns = format_suffix_patterns(urlpatterns)