from abc import ABC, abstractmethod


class BaseRequestHandler(ABC):

    @abstractmethod
    def handle(self, request):
        raise NotImplementedError("Subclass must implement the handle method !!!")
