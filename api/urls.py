from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView,DetailsView,CreateTagView, DetailTagView, CreateMemberView, DetailMemberView, CreatePostActivityView, DetailPostActivityView, CreateTodoView, DetailTodoView
urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^tag/$', CreateTagView.as_view(), name="create tag"),
    url(r'^tag/(?P<pk>[0-9]+)/$',
        DetailTagView.as_view(), name="details tag"),
    url(r'^member/$', CreateMemberView.as_view(), name="create member"),
    url(r'^member/(?P<pk>[0-9]+)/$',
        DetailMemberView.as_view(), name="details member"),
    url(r'^postactivity/$', CreatePostActivityView.as_view(), name="create post activity"),
    url(r'^postactivity/(?P<pk>[0-9]+)/$',
        DetailPostActivityView.as_view(), name="details post activity"),
    url(r'^todo/$', CreateTodoView.as_view(), name="create Todo"),
    url(r'^todo/(?P<pk>[0-9]+)/$',
        DetailTodoView.as_view(), name="details Todo"),
}

urlpatterns = format_suffix_patterns(urlpatterns)



