from django.test import TestCase

# Create your tests here.
# python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UploadLog
from django.core.files.uploadedfile import SimpleUploadedFile

class UploadLogTest(TestCase):
    def setUp(self):
        # Cria um usuário de teste com permissão de staff
        self.user = User.objects.create_user(username='testuser', password='12345', is_staff=True)
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_log_insertion(self):
        # Simula um upload de arquivo
        with open('testfile.txt', 'w') as f:
            f.write('conteúdo de teste')
        with open('testfile.txt', 'rb') as f:
            response = self.client.post('/upload/', {'file': SimpleUploadedFile(f.name, f.read())})

        # Verifica se o log foi inserido
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UploadLog.objects.filter(filename='testfile.txt').exists())