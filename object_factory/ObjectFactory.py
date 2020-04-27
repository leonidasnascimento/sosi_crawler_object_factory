from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from object_factory.domain.Dependecy import Dependency
from typing import Generic, TypeVar
from abc import ABC

import importlib
import json

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
        isNotSublcassMsg = "'{0}' not subclass of '{1}'"

        if not issubclass(interface, ABC):
            raise TypeError(isNotSublcassMsg.format(str(type(interface)), str(type(ABC))))

        if not issubclass(concreteClass, interface):
            raise TypeError(isNotSublcassMsg.format(str(type(concreteClass)), str(type(interface))))
        
        depCheck: [Dependency] = self.__findItem(targetCrawler, interface)

        if depCheck is not None:
            raise ValueError("Dependecy already set")
        else:
            dep: Dependency = Dependency(interface, targetCrawler, concreteClass)
            self.dependecies.append(dep)
        pass

    def LoadDependencies(self, filePath: str):
        """
        Load the dependencies that were predefined for SoSI's crawlers

        :param filePath: The pre defined dependencies file path
        :type filePath: str
        """

        attNotFoundMsg = "'{0}' attribute not found inside JSON file"

        if filePath is None or filePath == "":
            return

        with open(filePath) as jsonFile:
            preDefDependencies = json.load(jsonFile)

            if(preDefDependencies is None):
                return

            for dep in preDefDependencies:
                if "interface" not in dep:
                    raise AttributeError(attNotFoundMsg.format("interface"))
                
                if "implementation" not in dep:
                    raise AttributeError(attNotFoundMsg.format("implementation"))
                
                if "crawler" not in dep:
                    raise AttributeError(attNotFoundMsg.format("crawler"))

                interface = self.__import(dep["interface"])
                implementation = self.__import(dep["implementation"])
                crawler = dep["crawler"]

                self.AddDependency(crawler, interface, implementation)
                pass
            pass
        pass

    def GetInstance(self, targetCrawler: str, interface: Generic[InterfaceType]) -> InterfaceType:
        """
        Create an instance of a generic type accoding to a given interface & crawler alias

        :param interface: Interface type to be returned
        :param targetCrawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
        :type interface: Generic[InterfaceType]
        :type targetCrawler: str
        """
        dependency: Dependency = self.__findItem(targetCrawler, interface)

        if dependency is not None:
            return dependency.Implementation()
        else:
            return None
        pass
    
    def __import(self, package):
        components = package.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        
        return mod

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