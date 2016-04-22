from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^run/',views.run,name="run"),
    url(r'^save/',views.save,name='save'),
    url(r'^lang_change',views.lang_change,name='lang_change'),
    url(r'^$',views.index,name='CodeEditor'),
]
