from decouple import config
from stackapi import StackAPI
import datetime


class StackRequest:

    def __init__(self, endpoint, key, max_pages):
        self.site = StackAPI(endpoint, key=key)
        #self.site.max_pages = 100
        self.site.page_size = 100

    def run_query_question(self, endpoint, min, sort, filter, from_date, until_date):
        return self.site.fetch(endpoint=endpoint, filter=filter, order='asc', fromdate=str(datetime.datetime.timestamp(from_date)).replace(".0", ""), todate=str(datetime.datetime.timestamp(until_date)).replace(".0", ""))

    def run_query_answers(self, endpoint, ids, filter):
        return self.site.fetch(endpoint=endpoint, ids=ids, filter=filter)

