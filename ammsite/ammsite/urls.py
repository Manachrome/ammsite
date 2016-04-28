from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Роутинг приложения
#По регулярному выражению выбиратся какой шаблон использовать
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydjangosite.views.home', name='home'),
    # url(r'^mydjangosite/', include('mydjangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ammapp/$', 'ammapp.views.index'),
    url(r'^ammapp/group_detail/(?P<id>\d+)/$', 'ammapp.views.group_detail'),
    url(r'^ammapp/profile/(?P<id>\d+)/$', 'ammapp.views.profile'),
)
