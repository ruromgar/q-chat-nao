from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User, Group

import time


MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, NoSuchElementException, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)

        return modified_fn

    @wait
    def wait_for(self, fn):
        return fn()

    @wait
    def wait_for_element_to_exist(self, element_id):
        return self.browser.find_element_by_id(element_id)

    def login(self, username=None, group=None):
        self.browser.get('{0}{1}'.format(self.live_server_url, '/login/'))

        textbox_username = self.browser.find_element_by_id('id_username')
        textbox_password = self.browser.find_element_by_id('id_password')
        login_button = self.browser.find_element_by_xpath("//input[@type='submit']")

        user = User.objects.create_user(
            username=('ZiggyStardust' if username is None else username),
            first_name='David',
            last_name='Bowie',
            password='top_secret'
        )
        if group is not None:
            Group.objects.get_or_create(name=group)
            user.groups.add(Group.objects.get(name=group))
        textbox_username.send_keys(user.username)
        textbox_password.send_keys('top_secret')
        login_button.send_keys(Keys.RETURN)

        self.wait_for_element_to_exist('activities_home_page')

        return user

    def logout(self):
        self.browser.get('{0}{1}'.format(self.live_server_url, '/accounts/logout/'))
        self.wait_for(lambda: self.assertIn(
            'Successfully logged out',
            self.browser.find_element_by_id('content').text
        ))
