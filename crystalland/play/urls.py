from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'play.views.Main'),
    (r'^register/$', 'play.views.Register'),
    (r'^register/do$', 'play.views.DoRegister'),
    (r'^login/$', 'play.views.LoginPage'),
    (r'^login/do$', 'play.views.DoLogin'),
    (r'^logout/do$', 'play.views.DoLogout'),
    (r'^mercenaries/$', 'play.views.Mercenaries'),
    (r'^guild/create/do$', 'play.views.DoCreateGuild'),
    (r'^town/$', 'play.views.Town'),
    (r'^action/hire/$', 'play.views.DoHire'),
)
