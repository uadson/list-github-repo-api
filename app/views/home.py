import requests
import json

from django.views.generic import TemplateView

from app.models import Repository


class HomeView(TemplateView):
	template_name = 'app/index.html'
	context_object_name = 'data'

	def get_context_data(self, **kwargs):
		try:
			repos = Repository.objects.all()
			response = repos[0].data.values()
			context = super(HomeView, self).get_context_data(**kwargs)
			context['data'] = response
			return context
		except:
			response = {}
			context = super(HomeView, self).get_context_data(**kwargs)
			context['data'] = response
			return context 
