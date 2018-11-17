from django.conf.urls import url, include
from .views import all_features, feature_detail, add_or_edit_feature, delete_feature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^new/$', add_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_feature, name="edit_feature"),
    url(r'^(?P<pk>\d+)/delete/$', delete_feature, name="delete_feature"),
]