"""
    Module responsible to implement IObjectFactory
"""

from typing import Generic, TypeVar
from abc import ABC

import json

from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from object_factory.domain.dependecy import Dependency

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
        is_not_sublcass_msg = "'{0}' not subclass of '{1}'"

        if not issubclass(interface, ABC):
            raise TypeError(is_not_sublcass_msg.format(str(type(interface)), str(type(ABC))))

        if not issubclass(concreteClass, interface):
            raise TypeError(is_not_sublcass_msg.format(str(type(concreteClass)), str(type(interface))))

        dep_check: [Dependency] = self.__find_item(targetCrawler, interface)

        if dep_check is not None:
            raise ValueError('Dependecy already set')

        dep: Dependency = Dependency(interface, targetCrawler, concreteClass)
        self.dependecies.append(dep)

    def LoadDependencies(self, filePath: str):
        """
        Load the dependencies that were predefined for SoSI's crawlers

        :param filePath: The pre defined dependencies file path
        :type filePath: str
        """

        att_not_found_msg = "'{0}' attribute not found inside JSON file"

        if filePath is None or filePath == '':
            return

        with open(filePath) as json_file:
            pre_def_dependencies = json.load(json_file)

            if pre_def_dependencies is None:
                return

            for dep in pre_def_dependencies:
                if 'interface' not in dep:
                    raise AttributeError(att_not_found_msg.format('interface'))

                if 'implementation' not in dep:
                    raise AttributeError(att_not_found_msg.format('implementation'))

                if 'crawler' not in dep:
                    raise AttributeError(att_not_found_msg.format('crawler'))

                interface = self.__import(dep['interface'])
                implementation = self.__import(dep['implementation'])
                crawler = dep['crawler']

                self.AddDependency(crawler, interface, implementation)

    def GetInstance(self, targetCrawler: str, interface: Generic[InterfaceType]) -> InterfaceType:
        """
        Create an instance of a generic type accoding to a given interface & crawler alias

        :param interface: Interface type to be returned
        :param targetCrawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
        :type interface: Generic[InterfaceType]
        :type targetCrawler: str
        """
        dependency: Dependency = self.__find_item(targetCrawler, interface)

        if dependency is not None:
            return dependency.Implementation()

        return None

    def __import(self, package):
        components = package.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)

        return mod

    def __find_item(self, target_crawler: str, interface: Generic[InterfaceType]) -> Dependency:
        """
        Finds an item whithin the list

        :param target_crawler: Crawler
        :param interface: Interface
        :type target_crawler: str
        :param interface: Generic[InterfaceType]
        :return: [Dependency]
        """
        dep: Dependency = None

        if self.dependecies is not None:
            for dep in self.dependecies:
                if dep.Crawler.lower() == target_crawler.lower() and issubclass(dep.Interface, interface):
                    return dep

        return None
