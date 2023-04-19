from decouple import config
from stackapi import StackAPI

class StackRequest:

    def __init__(self, endpoint, key, max_pages):
        self.site = StackAPI(endpoint, key=key)
        self.site.max_pages = max_pages
        self.site.page_size = 10

    def run_query(self, endpoint, min, sort, filter):
        return self.site.fetch(endpoint=endpoint, min=min, sort=sort, filter=filter)

    def run_querytwo(self, endpoint, ids, filter):
        return self.site.fetch(endpoint=endpoint, ids=ids, filter=filter)

