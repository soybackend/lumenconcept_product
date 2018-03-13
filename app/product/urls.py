from django.conf.urls import url, include

from .views import (ProductViewSet, CategoryViewSet, MediaResourceViewSet,
                    schema_view)

api_url_patterns = [
    url(r'^categories/$', CategoryViewSet.as_view({
                                                   'get': 'list',
                                                   'post': 'create',
                                                  }), name='category-list'),
    url(r'^categories/(?P<pk>[0-9]+)$', CategoryViewSet.as_view({
                                                   'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'
                                                  }), name='category'),
    url(r'^mediaresources/$', MediaResourceViewSet.as_view({
                                                           'get': 'list',
                                                           'post': 'create',
                                                           }), name='media-list'),
    url(r'^mediaresources/(?P<pk>[0-9]+)$', MediaResourceViewSet.as_view({
                                                                         'get': 'retrieve',
                                                                         'put': 'update',
                                                                         'patch': 'partial_update',
                                                                         'delete': 'destroy'
                                                                         }), name='media'),
    url(r'^products/$', ProductViewSet.as_view({
                                               'get': 'list',
                                               'post': 'create',
                                               }), name='product-list'),
    url(r'^products/code/(?P<code>[\w-]+)$', ProductViewSet.as_view({
                                                         'get': 'retrieve_code'
                                                         }), name='product-retrieve'),
    url(r'^products/(?P<pk>[0-9]+)$', ProductViewSet.as_view({
                                                             'get': 'retrieve',
                                                             'put': 'update',
                                                             'patch': 'partial_update',
                                                             'delete': 'destroy'
                                                             }), name='product'),
]


urlpatterns = [
    url(r'^api/v1/', include(api_url_patterns)),
    url(r'^', schema_view),
]
