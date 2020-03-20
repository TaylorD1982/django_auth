{"filter":false,"title":"urls.py","tooltip":"/django_auth/urls.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":14,"column":0},"end":{"row":24,"column":1},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout, login, registration","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\"),","    url(r'^accounts/login/$', login, name=\"login\"),","    url(r'^accounts/register/$', registration, name=\"registration\")","]"],"id":42},{"start":{"row":14,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout, login, registration, user_profile","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\"),","    url(r'^accounts/login/$', login, name=\"login\"),","    url(r'^accounts/register/$', registration, name=\"registration\"),","    url(r'^accounts/profile/$', user_profile, name=\"profile\")","]"]}],[{"start":{"row":14,"column":0},"end":{"row":25,"column":1},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","from accounts.views import index, logout, login, registration, user_profile","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/logout/$', logout, name=\"logout\"),","    url(r'^accounts/login/$', login, name=\"login\"),","    url(r'^accounts/register/$', registration, name=\"registration\"),","    url(r'^accounts/profile/$', user_profile, name=\"profile\")","]"],"id":43},{"start":{"row":14,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts.views import index","from accounts import urls as accounts_urls","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/', include(accounts_urls))","]"]}],[{"start":{"row":14,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts.views import index","from accounts import urls as accounts_urls","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/', include(accounts_urls))","]"],"id":44},{"start":{"row":14,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts.views import index","from accounts import urls as accounts_urls","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/', include(accounts_urls))","]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":1},"end":{"row":23,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584172663665,"hash":"852cf605c08cb45f97fe57e751235ba312af0e1f"}