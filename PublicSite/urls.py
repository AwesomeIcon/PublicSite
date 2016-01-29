from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PublicSite.views.home', name='home'),
    # url(r'^PublicSite/', include('PublicSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.list'),
    url(r'^login/$','blog.views.login'),
    url(r'^blog/$','blog.views.submit'),
    url(r'^register/$','blog.views.register'),
    url(r'^blog/about/$','blog.views.about'),
    url(r'^logout/$', 'blog.views.logout'),
    url(r'^blog/add/$','blog.views.add'),
    url(r'^blog/article/$','blog.views.article'),
    url(r'^blog/single/(?P<num>\d+)/$','blog.views.single'),
    url(r'^blog/delete/$','blog.views.delete'),
    url(r'^blog/toedit/(?P<num>\d+)/$','blog.views.toedit'),
    url(r'^blog/edit/(?P<num>\d+)/$','blog.views.edit'),
    url(r'^blog/consult/$','blog.views.consult'),
)
