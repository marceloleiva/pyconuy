from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from tastypie.api import Api
from post.api.resources import PostResource, CommentResource

v1_api = Api(api_name='v1')
v1_api.register(PostResource())
v1_api.register(CommentResource())


urlpatterns = patterns('',
    
    url(r'^$', 'post.views.home', name='home'),
    url(r'^blog$', 'post.views.home', name='home'),
    url(r'^about$', 'post.views.home', name='home'),
    
    url(r'^api/', include(v1_api.urls)),
     
    url(r'^admin/', include(admin.site.urls)),
    
)

