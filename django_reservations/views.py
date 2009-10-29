import datetime, simplejson

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import permission_required, login_required

from schedule.models import Occurrence
from schedule.views import get_occurrence

from django_reservations.models import EventReservations

@login_required
def reservations(request, occurrence_id,
                         template_name='django_reservations/reservations.html'):
    """
    Displays all RSVPs for the given occurrence.
    """
    occurrence = get_object_or_404(Occurrence, pk=occurrence_id)
    try:
        er = occurrence.eventreservations
    except EventReservations.DoesNotExist:
        er = EventReservations(occurrence=occurrence)
        er.save()

    rsvpers = rs.reservations.all().order_by('last_name')

    context = RequestContext(request, {'occurrence': occurrence,
                                       'rsvpers': rsvpers})

    return render_to_response(template_name, context)

@login_required
def user_reservations(request, user_id=None, template_name='django_reservation/user_reservations.html'):
    """
    A reservation report for a specific user. Displays their reservation status
    for all RSVP-enabled occurrences in the future.
    """
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = request.user

    # 2-tuple of (calendar, [occurrences])
    cal_data = []
    for calendar in Calendar.objects.all():
        rsvped_occurrences = Occurrence.objects.filter(eventreservations__reservations=user, start__gt=datetime.datetime.now()).order_by('start')
        cal_data.append((calendar, rsvped_occurrences))

    context = RequestContext(request, dict(
        cal_data=cal_data,
        attendee=user
    ))

    return render_to_response(template_name, context)


@login_required
def rsvp(request, occurrence_id, template_name='django_reservations/rsvp.html'):
    """
    An rsvp page where the logged-in user can see their reservation status and
    modify it.
    """
    occurrence = get_object_or_404(Occurrence, pk=occurrence_id)

    result_msg = ''

    if request.method == "POST":
        form = RsvpForm(data=request.POST)
        if form.is_valid():
            occurrence = form.save()
            if form.cleaned_data['attending']:
                occurrence.eventreservations.reservations.add(request.user)
            else:
                try:
                    er = occurrence.eventreservations
                    er.remove(request.user)
                except EventReservations.DoesNotExist:
                    pass # no reservations exist, no need to remove anything

            return HttpResponseRedirect(reverse(
                'reservations_rsvp', kwargs={'occurrence_id':occurrence.pk}))
    else:
        form = RsvpForm(request)

    try:
        er = occurrence.eventreservations
        reserved = er.user_reserved(request.user)
    except EventReservations.DoesNotExist:
        reserved = False

    context = RequestContext(request, {'form':form, 'reserved':reserved})

    return render_to_response(template_name, context)

def rsvp_by_iso_date(request, event_id, iso_date):
    """
    Make an rsvp for an occurrence that hasn't yet been persisted.
    """
    t = datetime.datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S")
    event, occurrence = get_occurrence(event_id, year=t.year, month=t.month,
                                       day=t.day, hour=t.hour,
                                       minute=t.minute, second=t.second)
    occurrence.save()

    return rsvp(request, occurrence.pk)