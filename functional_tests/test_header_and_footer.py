from .base import FunctionalTest


class TestHeaderAndFooter(FunctionalTest):

    def test_footer_loads(self):
        # Footer should load if user is not authenticated
        self.browser.get(self.live_server_url)
        self.wait_for_element_to_exist('footer_text')

        # Footer should also load if user is authenticated
        self.login()
        self.browser.get(self.live_server_url)
        self.wait_for_element_to_exist('footer_text')

    def test_header_loads(self):
        # Header should have signup and login options if user is not authenticated
        self.browser.get(self.live_server_url)
        self.wait_for_element_to_exist('header_login')
        self.wait_for_element_to_exist('header_signup')

        # Header should have profile and logout options if user is authenticated
        self.login()
        self.browser.get(self.live_server_url)
        self.wait_for_element_to_exist('header_profile')
        self.wait_for_element_to_exist('header_logout')
