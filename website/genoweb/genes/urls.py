from django.conf.urls import url

from . import views
from views import IndexView,ListaGenes
urlpatterns = [
    url(r'^$', IndexView.as_view() ),
    url(r'^genes/$', ListaGenes.as_view(), name='ListaGenes')
]