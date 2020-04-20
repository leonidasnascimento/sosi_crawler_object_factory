from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from object_factory.domain.Dependecy import Dependency
from typing import Generic, TypeVar

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

        if not issubclass(concreteClass, interface):
            raise TypeError(type(concreteClass).__name__ + " not subclass of " + type(interface).__name__)

        dep: Dependency = Dependency(interface, targetCrawler, concreteClass) 

        if self.dependecies.index(dep) > -1:
            raise ValueError("Dependecy already set")

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
    pass