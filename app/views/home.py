from django.views.generic import TemplateView

from utils.get_api_data import GetApi

from app.models import Repository

from decouple import config


class HomeView(TemplateView):
	template_name = 'app/index.html'
	context_object_name = 'data'

	def get_context_data(self, **kwargs):

		context = super(HomeView, self).get_context_data(**kwargs)
		context['data'] = Repository.objects.all()

		return context
