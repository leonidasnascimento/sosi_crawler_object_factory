from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from object_factory.domain.Dependecy import Dependency
from typing import Generic, TypeVar
from abc import ABC

InterfaceType = TypeVar('InterfaceType')
ConcreteClassType = TypeVar('ConcreteClassType')

class ObjectFactory(IObjectFactory):
    """
    Concrete class for IObjectFactory interface. 
    """

    dependecies: [Dependency]

    def __init__(self):
        """
        Class initializer
        """

        self.dependecies = []
        pass

    def AddDependency(self, targetCrawler: str, interface: Generic[InterfaceType], concreteClass: Generic[ConcreteClassType]):
        """
        Add a generic type accoding to a given interface & crawler alias

        :param interface: Interface type to be returned
        :param targetCrawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
        :param concreteClass: Concrete class type that implements the interface
        :type concreteClass: ConcreteClassType
        :type interface: Generic[InterfaceType]
        :type targetCrawler: str
        """

        if not issubclass(interface, ABC):
            raise TypeError(type(interface).__name__ + " not subclass of " + type(ABC).__name__)

        if not isinstance(concreteClass, interface):
            raise TypeError(type(concreteClass).__name__ + " not an instance of " + type(interface).__name__)
        
        depCheck: [Dependency] = self.__findItem(targetCrawler, interface)

        if depCheck is not None:
            raise ValueError("Dependecy already set")
        else:
            dep: Dependency = Dependency(interface, targetCrawler, concreteClass)
            self.dependecies.append(dep)
        pass

    def LoadPredefinedDependencies(self):
        """
        Load the dependencies that were predefined for SoSI's crawlers
        """
        pass

    def GetInstance(self, targetCrawler: str, interface: Generic[InterfaceType]) -> InterfaceType:
        """
        Create an instance of a generic type accoding to a given interface & crawler alias

        :param interface: Interface type to be returned
        :param targetCrawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
        :type interface: Generic[InterfaceType]
        :type targetCrawler: str
        """ 
    
    def __findItem(self, targetCrawler: str, interface: Generic[InterfaceType]) -> Dependency:
        """
        Finds an item whithin the list

        :param targetCrawler: Crawler
        :param interface: Interface
        :type targetCrawler: str
        :param interface: Generic[InterfaceType]
        :return: [Dependency]
        """
        dep: Dependency = None

        if self.dependecies is not None:
            for dep in self.dependecies:
                if dep.Crawler.lower() == targetCrawler.lower() and issubclass(dep.Interface, interface):
                    return dep
                pass
            pass

        return None
    pass