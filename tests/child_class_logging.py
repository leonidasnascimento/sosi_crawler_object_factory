from sosi_crawler_interfaces.ILogging import ILogging
from sosi_crawler_interfaces.IDataRepository import IDataRepository

class ChildClassILogging(ILogging):
    def __init__(self):
        pass

    def SetRepository(self, repository: IDataRepository): raise NotImplementedError
    """
    Sets a repository in order to use within logging process

    :param repository: A repository object
    :type repository: IDataRepository
    """

    def Log(self, message: str):
        """
        Performs log operation

        :param messagem: A message to log
        :type message: str
        """
        print(str("MOCK: '{0}'").format(message))
        pass
    pass
