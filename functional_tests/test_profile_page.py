from .base import FunctionalTest


class TestProfilePage(FunctionalTest):

    def test_profile_page_loads(self):
        # Should be accessible and show Patient Dashboard if the user is authenticated as a Patient
        self.login(group='Patients')
        self.browser.get('{0}{1}'.format(self.live_server_url, '/accounts/profile/'))
        self.wait_for(lambda: self.assertIn(
            'Patient Dashboard',
            self.browser.find_element_by_id('content').text
        ))
        self.logout()

        # Should be accessible and show Therapist Dashboard if the user is authenticated as a Therapist
        # Note: Providing username to avoid database IntegrityError "UNIQUE constraint failed: auth_user.username"
        self.login(username='TheThinWhiteDuke', group='Therapists')
        self.browser.get('{0}{1}'.format(self.live_server_url, '/accounts/profile/'))
        self.wait_for(lambda: self.assertIn(
            'Therapist Dashboard',
            self.browser.find_element_by_id('content').text
        ))
        self.logout()

        # Should not be accessible if the user is not authenticated
        self.browser.get('{0}{1}'.format(self.live_server_url, '/accounts/profile/'))
        self.wait_for(lambda: self.assertNotIn(
            'Dashboard',
            self.browser.find_element_by_id('content').text
        ))
