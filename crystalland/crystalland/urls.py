from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crystalland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url( r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #                                        { 'document_root':settings.STATIC_ROOT }),
    url(r'^test/(\d+)vs(\d+)', 'gamecore.views.testbattle'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dungeon/show/$', 'gamecore.views.showdungeon'),
    url(r'^dungeon/add/$', 'gamecore.views.adddungeon'),
    url(r'^dungeon/del/(\d+)/$', 'gamecore.views.deldungeon'),
    url(r'^dungeon/mod/(\d+)/$', 'gamecore.views.moddungeon'),
    url(r'^dungeon/mod/monadd/$', 'gamecore.views.addmonster'),
    url(r'^dungeon/mod/mondel/$', 'gamecore.views.delmonster'),
    url(r'^dungeon/mod/monmod/$', 'gamecore.views.modmonster'),
)
