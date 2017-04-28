# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from genes.models import PhenoDb
from genes.forms import PhenoDBForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

class IndexView(CreateView):
	model = PhenoDb
	form_class = PhenoDBForm


class ListaGenes(ListView):
    template_name = 'genes/genes.html'
    model = PhenoDb
    # paginate_by = 100
    def get_context_data(self, **kwargs):
		
		doencas =  self.request.GET['disease']
		doencas = doencas.split(",")
		context = super(ListaGenes, self).get_context_data(**kwargs)
		genes = []
		for doenca in doencas:
			doenca = doenca.strip()
			genes.append({'doenca': doenca ,'genes' : PhenoDb.objects.all().filter(disease__iexact = doenca)})
		context.update({'doencasT' : genes})
		
		return context

