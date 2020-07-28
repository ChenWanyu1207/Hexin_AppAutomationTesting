import pytest

from driver.app import App
import yaml

class TestSearch:
    with open("../data/search.yaml") as data:
        contents = data.read()
    search_data = yaml.safe_load(contents)
    def setup(self):
        self.search_page = App.start().to_search()

    @pytest.mark.parametrize("keywords", search_data)
    def test_search_join_or_delete(self,keywords):
        self.search_page.search(keywords).stock_join_or_delete()
        assert "自选股" in self.search_page.toast_join_or_delete()
        print(self.search_page.toast_join_or_delete())


    def teardown(self):
        App.quit()







