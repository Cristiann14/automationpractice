class BasePage(object):

    url = None  # class atribute

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    @property
    def get_url(self):
        url = self.driver.current_url
        return url
