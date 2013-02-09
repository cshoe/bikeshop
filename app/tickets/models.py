import logging

from django.conf import settings
from django.db import models


logger = logging.getLogger(__name__)


TICKET_STATUS_CODES = (
    (1, 'New'),
    (2, 'Assigned'),
    (3, 'Blocked'),
    (4, 'Done'),
    (5, 'Picked up')
)


class Ticket(models.Model):
    """
    Model work that needs to be done in the shop.
    """
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        db_index=True,
        null=True)

    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    status = models.IntegerField(default=1, choices=TICKET_STATUS_CODES)
    description = models.TextField(blank=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_due = models.DateField(blank=True)


class TicketComment(models.Model):
    """
    Model for comments that are left on a ticket.
    """
    ticket = models.ForeignKey(Ticket)
    commentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='commenter'
    )
    content = models.TextField()
