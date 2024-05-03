from .service_integration.counter_service_integration import CounterServiceIntegration
from .short_url_genrator import generate_base62_string
from .data_store import URLStore, RecordExistsException, NoDataFound
from flask import redirect


class TinyUrl:
    MAX_COUNTER = None
    COUNTER = None

    def submit_long_url(self, long_url: str):
        try:
            tiny_url = generate_base62_string(self.COUNTER)
            self.COUNTER += 1
            data = {"originalUrl": long_url, "shortUrl": tiny_url}
            URLStore.insert(data)
        except RecordExistsException as e:
            print(str(e))
            self.submit_long_url(long_url)  # retry to with a new counter

    @classmethod
    def get_long_url(cls, tiny_url: str):
        try:
            long_url = URLStore.get(tiny_url)
            return long_url
        except NoDataFound:
            print("No tiny url for the passed short url")

    @classmethod
    def set_counter_range(cls):
        cls.COUNTER, cls.MAX_COUNTER = CounterServiceIntegration.get_counter_range()

    @classmethod
    def check_and_update_counter(cls):
        if cls.COUNTER >= cls.MAX_COUNTER:
            cls.set_counter_range()

    @classmethod
    def redirect_url(cls, tiny_url: str):
        long_url = cls.get_long_url(tiny_url)
        if long_url:
            print(f"redirecting to long url = {long_url}")
            return redirect(long_url)
