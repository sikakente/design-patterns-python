import abc


class AbsFactory(abc.ABC):
    @abc.abstractmethod
    def create_auto(self):
        raise NotImplementedError("Must implement create auto")
