from utils.singleton_meta import SingletonMeta


class Configuration(metaclass=SingletonMeta):
    """
    Contains constants that can configure the test execution
    """
    WAIT_10 = 10


config = Configuration()
