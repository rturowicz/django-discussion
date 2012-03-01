from django.conf.urls.defaults import *
from django.views.generic import RedirectView

from discussion.views import (DiscussionList, DiscussionView,
                              CreatePost, PostList, PostView,
                              Search)


urlpatterns = patterns('discussion.views',
    url(r'^$', DiscussionList.as_view(), name='home'),
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^discussions/', include(patterns('',
        url(r'^$', RedirectView.as_view(url='../')),
        url(r'^(?P<slug>[\w-]+)/$', DiscussionView.as_view(), name='discussion'),
        url(r'^(?P<discussion_slug>[\w-]+)/posts/$', PostList.as_view(), name='list-post'),
        url(r'^(?P<discussion_slug>[\w-]+)/posts/add/$', CreatePost.as_view(), name='create-post'),
        url(r'^(?P<discussion_slug>[\w-]+)/posts/(?P<slug>[\w-]+)/$', PostView.as_view(), name='post'),
    )))
)
