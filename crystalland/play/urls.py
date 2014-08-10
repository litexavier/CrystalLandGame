from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'play.views.Main'),
    (r'^register/$', 'play.views.Register'),
    (r'^register/do$', 'play.views.DoRegister'),
    (r'^login/$', 'play.views.LoginPage'),
    (r'^login/do$', 'play.views.DoLogin'),
    (r'^logout/do$', 'play.views.DoLogout'),
    (r'^mercenaries/$', 'play.views.Mercenaries'),
    (r'^mercenaries/members/$', 'play.views.MercenariesMembers'),
    (r'^mercenaries/members/show/do$', 'play.views.GetMemberDetail'),
    (r'^guild/create/do$', 'play.views.DoCreateGuild'),
    (r'^town/$', 'play.views.Town'),
    (r'^town/hire/$', 'play.views.Hire'),
    (r'^town/hire/do$', 'play.views.DoHire')
)
