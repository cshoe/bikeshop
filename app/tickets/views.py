import logging

from annoying.decorators import render_to
from django.shortcuts import get_object_or_404

from .models import Ticket


logger = logging.getLogger(__name__)


@render_to('ticets/single_ticket.html')
def single_ticket(request, ticket_id):
    """
    Display a single Ticket.

    """
    ticket = get_object_or_404(Ticket, id=ticket_id)

    context = {
        'ticket': ticket
    }

    return context
