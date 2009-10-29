from django.conf.urls.defaults import *

urlpatterns = patterns('django_reservations.views',

# Already-persisted occurrence
url(r'^(?P<occurrence_id>\d+)/$',
    'reservations',
    name="reservations_reservations_view"),

url(r'^(?P<occurrence_id>\d+)/rsvp/$',
    'rsvp',
    name="reservations_rsvp"),

# Non-persisted occurrence
url(r'^(?P<event_id>\d+)/(?P<iso_date>[-:\w]+)/rsvp/$',
    'rsvp_by_iso_date',
    name="reservations_rsvp_by_iso_date"),

# Reports
url(r'^mine/$',
    'user_reservations',
    name="reservations_reservations_mine"),
url(r'^user/(?P<user_id>\d+)/$',
    'user_reservations',
    name="reservations_reservations_for_user"),

)