import logging
log = logging.getLogger(__name__)

from pyramid.view import view_config
import pyramid.httpexceptions as exception


@view_config(
    route_name='client.list',
    renderer='saas.app:templates/client/list.html',
    request_method='GET'
)
def view_client_list(request):
    destination = request.params['destination'] if 'destination' in request.params else ''

    session = request.session
    email = session['email'] if 'email' in session else ''

    if email == '':
        # user is not logged in, redirect to sign in page
        raise exception.HTTPFound(request.route_url('security.signin'))

    services = request.services()
    userStore = services['store.user']
    user = userStore.userByEmail(email)
    user_id = user[0]
    clients = userStore.userClients(user_id)

    return {
        'destination': destination,
        'clients': clients
    }

@view_config(
    route_name='client.select',
    request_method='GET',
    permission='user.authenticated'
)
def view_client_select(request):
    client_id = request.matchdict['client_id'] if 'client_id' in request.matchdict else ''

    session = request.session
    session['client'] = client_id

    raise exception.HTTPFound(request.route_url('home'))
    return {}

@view_config(
    route_name='client.join',
    request_method='GET',
    renderer='saas.app:templates/client/join.html',
    permission='user.authenticated'
)
def view_client_join(request):
    return {}