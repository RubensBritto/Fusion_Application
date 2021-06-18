from django.contrib import messages
from django.views.generic import FormView
from .models import Servico, Funcionario, Feature
from .forms import ContatoForms
from django.urls import reverse_lazy

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForms
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['feature'] = Feature.objects.order_by('?').all()
        context['cont1'] = str(Feature.objects.count()//2) + ':'
        context['cont2'] = ':' + str(Feature.objects.count()//2)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error ao enviar o E-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

