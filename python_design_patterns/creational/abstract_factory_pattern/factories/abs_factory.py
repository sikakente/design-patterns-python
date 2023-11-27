import abc


class AbsFactory(abc.ABC):
    @abc.abstractstaticmethod
    def create_economy():
        raise NotImplementedError()

    @abc.abstractstaticmethod
    def create_sport():
        raise NotImplementedError()

    @abc.abstractstaticmethod
    def create_luxury():
        raise NotImplementedError()
