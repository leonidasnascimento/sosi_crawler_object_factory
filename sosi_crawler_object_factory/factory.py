"""
    Module responsible to implement IObjectFactory
"""

from typing import Generic, TypeVar
from abc import ABC

import json

from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_object_factory.dependecy import Dependency

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

    def AddDependency(self, target_crawler: str, interface: Generic[InterfaceType], concrete_class: Generic[ConcreteClassType]):
        """
        Add a generic type accoding to a given interface & crawler alias

        :param interface: Interface type to be returned
        :param target_crawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
        :param concrete_class: Concrete class type that implements the interface
        :type concrete_class: ConcreteClassType
        :type interface: Generic[InterfaceType]
        :type target_crawler: str
        """
        is_not_sublcass_msg = "'{0}' not subclass of '{1}'"

        if not issubclass(interface, ABC):
            raise TypeError(is_not_sublcass_msg.format(str(type(interface)), str(type(ABC))))

        if not issubclass(concrete_class, interface):
            raise TypeError(is_not_sublcass_msg.format(str(type(concrete_class)), str(type(interface))))

        dep_check: [Dependency] = self.__find_item(target_crawler, interface)

        if dep_check is not None:
            raise ValueError('Dependecy already set')

        dep: Dependency = Dependency(interface, target_crawler, concrete_class)
        self.dependecies.append(dep)

    def LoadDependencies(self, file_path: str):
        """
        Load the dependencies that were predefined for SoSI's crawlers

        :param file_path: The pre defined dependencies file path
        :type file_path: str
        """

        att_not_found_msg = "'{0}' attribute not found inside JSON file"

        if file_path is None or file_path == '':
            return

        with open(file_path) as json_file:
            pre_def_dependencies = json.load(json_file)

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

    def GetInstance(self, target_crawler: str, interface: Generic[InterfaceType]) -> InterfaceType:
        """
        Create an instance of a generic type accoding to a given interface & crawler alias

        :param interface: Interface type to be returned
        :param target_crawler: Target crawler alias. It'll help the Object Factory to find the concrete class to inject
        :type interface: Generic[InterfaceType]
        :type target_crawler: str
        """
        dependency: Dependency = self.__find_item(target_crawler, interface)

        if dependency is not None:
            return dependency.implementation()

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
                if dep.crawler.lower() == target_crawler.lower() and issubclass(dep.interface, interface):
                    return dep

        return None
