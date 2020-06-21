from .base import FunctionalTest


class TestHomePage(FunctionalTest):

    def test_home_page_loads(self):
        # Should not be available if user is not authenticated
        self.browser.get(self.live_server_url)
        self.wait_for(lambda: self.assertNotIn(
            'Available activities',
            self.browser.find_element_by_id('content').text
        ))

        # Should be available if user is authenticated
        # Note: login() function already uses 'activities_home_page' as assertion
        self.login()

    def test_modal_pops_up_and_starts_activity(self):
        self.login()
        for i in range(1, 7):
            # All modal/buttons inside have names based on this format: activityXXmodal_ACTION
            modal_name = 'activity{0}modal'.format('{:02}'.format(i))

            self.browser.find_element_by_id('btn_{0}'.format(modal_name)).click()
            self.wait_for(lambda: self.assertTrue(self.browser.find_element_by_id(modal_name).is_displayed()))
            self.browser.find_element_by_id('{0}_start'.format(modal_name)).click()

            self.wait_for(lambda: self.assertIn(
                'Activity {0}'.format('{:02}'.format(i)),
                self.browser.find_element_by_id('content').text
            ))

            self.browser.get(self.live_server_url)
            self.wait_for(lambda: self.assertIn(
                'Available activities',
                self.browser.find_element_by_id('content').text
            ))

    def test_can_start_activity_from_main_page(self):
        self.login()
        for i in range(1, 7):
            # All modal/buttons inside have names based on this format: activityXXmodal_ACTION
            btn_name = 'btn_activity{0}_start'.format('{:02}'.format(i))

            self.browser.find_element_by_id(btn_name).click()
            self.wait_for(lambda: self.assertIn(
                'Activity {0}'.format('{:02}'.format(i)),
                self.browser.find_element_by_id('content').text
            ))

            self.browser.get(self.live_server_url)
            self.wait_for(lambda: self.assertIn(
                'Available activities',
                self.browser.find_element_by_id('content').text
            ))
