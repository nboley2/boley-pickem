from base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_create_new_account(self):
        # A user comes to the site and is able to view the home page
        self.browser.get(self.live_server_url)

        # The page title is Boley Pick 'Em
        self.assertIn("Boley Pick 'Em", self.browser.title)

        # The user notices a log in option and a link to create an account
