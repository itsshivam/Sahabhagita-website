from django.conf.urls import url
from django.contrib import admin

from .views import (
		index,
		signup,
		details,
		Login,
		home,
		gallery,
		logIn,
		signcheck,
		auth_view,
		logOut,
		formcheck,
		formcheck2,
		formcheck3,
		formcheck4,
		member,
		feedbackmake,
		contact,
		commentmake,
	)

urlpatterns = [
    url(r'^$', index),
    url(r'^signup/$', signup),
    url(r'^signUp/$', signcheck),
    url(r'^details/$', details),
    url(r'^Details/$', formcheck),

    url(r'^login/$', Login),
   	url(r'^logIn/$', logIn),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logOut),

    url(r'^home/$', home),
    url(r'^gallery/$', gallery),
    url(r'^members/$', member),
    url(r'^feedback/$', feedbackmake),
    url(r'^Contact/$', formcheck2),
    url(r'^contact/$', contact),
    url(r'^comment/$', commentmake),
    url(r'^Comment/$', formcheck3),
    url(r'^Comment/$', formcheck3),
    url(r'^Feedback/$', formcheck4),
    
  ]