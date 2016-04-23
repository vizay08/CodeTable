from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^run/',views.run,name="run"),
    url(r'^save/',views.save,name='save'),
    url(r'^lang_change',views.lang_change,name='lang_change'),
    url(r'^sforshare',views.generate_share_url,name='share_url'),
    url(r'^(?P<token>[a-zA-Z0-9]{6})/',views.serve_token_url,name='serve_url'),
    url(r'^$',views.index,name='CodeEditor'),
]
