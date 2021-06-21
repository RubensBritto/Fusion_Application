from django.test import TestCase, Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Rubens Brito',
            'email': 'rubens@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Hey Brother'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
    
    def test_form_invalid(self):
        dados = {
            'nome': 'Rubens Brito',
            'email': 'rubens@gmail.com',
        }
        
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)

