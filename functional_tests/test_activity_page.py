from django.contrib.auth.models import User, Group
from .base import FunctionalTest
from unittest import skip

class TestActivityPage(FunctionalTest):

    def test_activity_pages_load(self):
        # None of them should be accessible if the user is not authenticated
        for i in range(1, 7):
            self.browser.get('{0}{1}{2}'.format(self.live_server_url, '/activity', '{:02}/'.format(i)))
            self.wait_for(lambda: self.assertNotIn(
                'Activity {0}'.format('{:02}'.format(i)),
                self.browser.find_element_by_id('content').text
            ))

        # All of them should be accessible if the user is authenticated
        self.login()
        for i in range(1, 7):
            self.browser.get('{0}{1}{2}'.format(self.live_server_url, '/activity', '{:02}/'.format(i)))
            self.wait_for(lambda: self.assertIn(
                'Activity {0}'.format('{:02}'.format(i)),
                self.browser.find_element_by_id('content').text
            ))

    @skip
    def test_activity_page_loads_patients(self):
        user = self.login(group='Patients')
        for i in range(1, 7):
            self.browser.get('{0}{1}{2}'.format(self.live_server_url, '/activity', '{:02}/'.format(i)))
            dropdown = self.browser.find_element_by_id('dropdown_patient')
            pat_username = self.browser.find_element_by_id('pat_username')
            pat_fullname = self.browser.find_element_by_id('pat_fullname')

            # The user should be in the dropdown options, since it is a Patient
            options = dropdown.find_elements_by_tag_name('option')
            self.wait_for(lambda: self.assertIn(
                user.username,
                ' '.join(o.text for o in options)
            ))

            # If no user is selected, details should be empty
            self.wait_for(lambda: self.assertEqual('', pat_username.text))
            self.wait_for(lambda: self.assertEqual('', pat_fullname.text))

            # After selecting a user, its details should appear
            for o in options:
                if o.text == user.username:
                    o.click()
            self.wait_for(lambda: self.assertIn(
                user.username,
                pat_username.text
            ))
            self.wait_for(lambda: self.assertIn(
                '{0} {1}'.format(user.first_name, user.last_name),
                pat_fullname.text
            ))
