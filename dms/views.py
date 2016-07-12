from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session


@login_required
def index(request):
    session = Session.objects.all().first()

    return render_to_response('index.jinja', {
        'user': request.user,
        'session_info': None if session is None else session.get_decoded(),
        'distribution': 'arch'})
