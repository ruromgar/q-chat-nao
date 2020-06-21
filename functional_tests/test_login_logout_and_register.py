from selenium.webdriver.common.keys import Keys

from django.contrib.auth.models import User, Group
from django.core import mail
from django.conf import settings

from .base import FunctionalTest

import re


class TestLoginLogoutAndRegister(FunctionalTest):

    def test_can_login_and_logout(self):
        self.browser.get('{0}{1}'.format(self.live_server_url, '/login/'))

        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        login_button = self.browser.find_element_by_xpath("//input[@type='submit']")

        User.objects.create_user(username='username', password='top_secret')
        username.send_keys('username')
        password.send_keys('top_secret')
        login_button.send_keys(Keys.RETURN)

        self.wait_for_element_to_exist('activities_home_page')

        self.browser.get('{0}{1}'.format(self.live_server_url, '/accounts/logout/'))
        self.wait_for(lambda: self.assertIn(
            'Successfully logged out',
            self.browser.find_element_by_id('content').text
        ))

    def test_can_register_and_get_activation_mail(self):
        Group.objects.get_or_create(name='new_group')
        self.browser.get('%s%s' % (self.live_server_url, '/accounts/register/'))

        username = self.browser.find_element_by_id('id_username')
        email = self.browser.find_element_by_id('id_email')
        password1 = self.browser.find_element_by_id('id_password1')
        password2 = self.browser.find_element_by_id('id_password2')
        group = self.browser.find_element_by_id('id_group')
        submit = self.browser.find_element_by_xpath("//input[@type='submit']")

        username.send_keys('name')
        email.send_keys('mail@mail.com')
        password1.send_keys('top_secret')
        password2.send_keys('top_secret')
        for option in group.find_elements_by_tag_name('option'):
            if option.text == 'new_group':
                option.click()
        submit.send_keys(Keys.RETURN)

        # Everything needed is provided, so it should send a mail
        self.wait_for(lambda: self.assertIn(
            'Activation email sent',
            self.browser.find_element_by_id('content').text
        ))

        # And it is actually sending it - checking also subject and days until expire date
        email = mail.outbox[0]
        self.assertIn('mail@mail.com', email.to)
        self.assertIn(settings.REGISTRATION_EMAIL_SUBJECT_PREFIX, email.subject)
        self.assertIn(
            'click the following link within the next\n{0} days'.format(settings.ACCOUNT_ACTIVATION_DAYS),
            email.body
        )

        # It has a url link in it to activate the account
        url_search = re.search(r'http://.+/accounts/activate/.+/', email.body)
        if not url_search:
            self.fail('Could not find url in email body:\n{0}'.format(email.body))
        url = url_search.group(0)

        # Clicking the url changes the account status to active
        self.browser.get(url)
        self.wait_for(lambda: self.assertIn(
            'Account Activated',
            self.browser.find_element_by_id('content').text
        ))

    def test_register_without_selecting_group_is_not_allowed(self):
        self.browser.get('{0}{1}'.format(self.live_server_url, '/accounts/register/'))

        username = self.browser.find_element_by_id('id_username')
        email = self.browser.find_element_by_id('id_email')
        password1 = self.browser.find_element_by_id('id_password1')
        password2 = self.browser.find_element_by_id('id_password2')
        submit = self.browser.find_element_by_xpath("//input[@type='submit']")

        username.send_keys('name')
        email.send_keys('mail@mail.com')
        password1.send_keys('top_secret')
        password2.send_keys('top_secret')
        submit.send_keys(Keys.RETURN)

        # Group, being required, is not provided, so it should not send any mail
        self.wait_for(lambda: self.assertNotIn(
            'Activation email sent',
            self.browser.find_element_by_id('content').text
        ))
