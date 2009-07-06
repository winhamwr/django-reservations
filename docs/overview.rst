========
Overview
========

----
Goal
----

Django-reservations doesn't manage or create events. You should use something else for that. This app has very narrow goals:

 * Users can mark themselves as attending, not attending or maybe attending an event (their `reservation`)
 * Users can see reservations
 * Users can limit the number of people able to register

------
Status
------

Django-reservations is alpha software. I'm implementing the feature specifically to work with django-schedule, but with the mindset that anything that defines an event should be able to work. 
