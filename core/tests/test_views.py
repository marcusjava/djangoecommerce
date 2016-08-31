from django.test import TestCase,Client
'''usado para chamar a view pelo nome'''
form django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

    '''metodo inicial'''
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    '''metodo para finalizar o teste'''
    def tearDown(self):
        pass

    def test_status_code(self):
        client = Client()
        response = client.get(self.url)
        self.assertEquals(response.status_code,200)

    def test_template_used(self):
        client = Client()
        response = client.get(self.url)
        self.assertTemplateUsed(response,'index.html')
