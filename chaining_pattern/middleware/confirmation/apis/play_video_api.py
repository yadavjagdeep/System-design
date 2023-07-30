from ..factories.request_handler_factory import RequestHandlerFactory


class PlayVideoApi:

    def process_request(self, request):
        RequestHandlerFactory.get_request_handler(api_name="play_video").handle(request)
        print(f"Processing request for {self.__class__.__name__} started ... ")
        return
