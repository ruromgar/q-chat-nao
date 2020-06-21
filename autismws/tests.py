from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User, Group

from activities.views import home


class HomePageTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(id='1', username='name', email='e@e.com', password='top_secret')

    def test_anonymous_user_gets_redirected_to_login_page(self):

        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = home(request)

        redirect_url = dict(response.items())['Location']

        # If true, we're redirecting to the login view
        self.assertEqual(response.status_code, 302)
        self.assertEqual(redirect_url, '/login/')

    def test_user_gets_access_to_home_page(self):
        self.client.login(username='name', password='top_secret')
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'activities/home.html')



