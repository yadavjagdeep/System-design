from abc import ABC, abstractmethod


class BaseHandler(ABC):

    @abstractmethod
    def handle(self, request):
        raise NotImplementedError("Subclass must implement the handle method !!!")
