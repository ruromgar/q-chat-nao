from .base import FunctionalTest


class TestNaoSpeechAndAction(FunctionalTest):

    def test_nao_speech_does_nothing_when_accessed_directly(self):
        # Should not be accessible if the user is not authenticated - redirects to login page
        self.browser.get('{0}{1}'.format(self.live_server_url, '/nao_speech/'))
        self.wait_for(lambda: self.assertIn(
            'Log in',
            self.browser.find_element_by_id('content').text
        ))

        # Should not be accessible if the user is authenticated - redirects to home page
        self.login()
        self.browser.get('{0}{1}'.format(self.live_server_url, '/nao_speech/'))
        self.wait_for(lambda: self.assertIn(
            'Available activities',
            self.browser.find_element_by_id('content').text
        ))

    def test_nao_action_does_nothing_when_accessed_directly(self):
        # Should not be accessible if the user is not authenticated - redirects to login page
        self.browser.get('{0}{1}'.format(self.live_server_url, '/nao_action/'))
        self.wait_for(lambda: self.assertIn(
            'Log in',
            self.browser.find_element_by_id('content').text
        ))

        # Should not be accessible if the user is authenticated - redirects to home page
        self.login()
        self.browser.get('{0}{1}'.format(self.live_server_url, '/nao_action/'))
        self.wait_for(lambda: self.assertIn(
            'Available activities',
            self.browser.find_element_by_id('content').text
        ))
