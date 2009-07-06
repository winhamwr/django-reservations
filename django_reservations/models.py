from django.contrib.contenttypes import generic
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User

reservation_statuses = (("ATTENDING", _("Attending")),
                        ("NOT ATTENDING", _("Not Attending")),
                        ("UNSURE", _("Unsure")),)

class Reservation(models.Model):
    '''
    The reservation status of a user for an event.
    '''
    event = generic.GenericForeignKey('event_content_type', 'event_object_id')
    event_content_type = models.ForeignKey(ContentType)
    event_object_id = models.IntegerField()
    user = models.ForeignKey(User)
    status = models.CharField(_("reservation status"),
                              choices=reservation_statuses, default=None,
                              null=True, blank=True, max_length=20)

    class Meta:
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')

    def __unicode__(self):
        return "%s reservation for %s" % (self.event, self.user)