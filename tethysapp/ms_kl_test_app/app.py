from tethys_sdk.base import TethysAppBase, url_map_maker


class MsKlTestApp(TethysAppBase):
    """
    Tethys app class for ms kl test app.
    """

    name = 'ms kl test app'
    index = 'ms_kl_test_app:home'
    icon = 'ms_kl_test_app/images/icon.gif'
    package = 'ms_kl_test_app'
    root_url = 'ms-kl-test-app'
    color = '#1abc9c'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='ms-kl-test-app',
                           controller='ms_kl_test_app.controllers.home'),
        )

        return url_maps