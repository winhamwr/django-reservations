from django import forms

from schedule.models import Occurrence

from django_reservations.models import EventReservations

class RsvpForm(forms.ModelForm):
    attending = forms.BooleanField(default=True, required=False)

    def clean(self):
        data = self.cleaned_data

        if data['attending']:
            try:
                er = self.instance.eventreservations
            except EventReservations.DoesNotExist:
                er = EventReservations(occurrence=self.instance)
                er.save()

                if not er.can_rsvp():
                    raise forms.ValidationError("RSVP limit reached. This event is full")

    class Meta:
        model = Occurrence
        exclude = ('event', 'title', 'description', 'start', 'end', 'cancelled', 'original_start', 'original_end')