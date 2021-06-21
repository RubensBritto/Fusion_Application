from unittest.result import failfast
from django.test import TestCase
from core.forms import ContatoForms

class ContatoFormTestCase(TestCase):
    def setUp(self):
        self.nome = "Felicity Jones"
        self.email = 'felicity@gmail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Ola meu amigo'
        
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForms(data=self.dados)  #ContatoForms(request.POST)

    def test_send_mail(self):
        form1 = ContatoForms(data=self.dados)
        form1.is_valid()    
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEquals(res1, res2)