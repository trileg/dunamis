from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.sessions.models import Session


@login_required
def index(request):
    session = Session.objects.all().first()

    return render_to_response('index.jinja', {
        'session_info': None if session is None else session.get_decoded(),
        'distribution': 'arch'})
