
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
class AuthRequiredMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.user.is_authenticated() and request.path.strip('/')!='login':
			return HttpResponseRedirect(reverse('login')) # or http response
		else:
			return self.get_response(request)
		