from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import admin

from schedule.models import Occurrence

class EventReservations(models.Model):
    """
    Reservation settings for an occurrence.
    """
    occurrence = models.OneToOneField(Occurrence)
    reservation_limit = models.IntegerField(default=0) # 0 is no limit
    reservations = models.ManyToManyField(User, blank=True)


    class Meta:
        verbose_name = _('Event Reservation')
        verbose_name_plural = _('Event Reservations')

    def __unicode__(self):
        return "reservation settings for %s" % self.occurrence

    def user_reserved(self, user):
        """
        Determine whether a user has confirmed yes for this occurrence.
        """
        count = self.reservations.filter(pk=user.pk).count()
        if count > 0:
            return True
        else:
            return False

    def has_limit(self):
        return self.reservation_limit != 0

    def can_rsvp(self):
        """
        Can another user RSVP yes or are we at our reservation_limit?
        """
        if self.reservation_limit <= 0:
            return True

        count = self.reservations.count()
        if count >= self.reservation_limit:
            return False

        return True

admin.site.register(EventReservations)
