from typing import Generic, TypeVar

InterfaceType = TypeVar('InterfaceType')
ConcreteObjType = TypeVar('ConcreteObjType')

class Dependency():
    """
    Domain class that represents a dependency configuration
    """

    Interface: InterfaceType
    Crawler: str
    Implementation: ConcreteObjType

    def __init__(self, interface: Generic[InterfaceType], crawler: str, implementation: Generic[ConcreteObjType]):
        """
        Class initializer

        :param interface: Interface that should be implemented
        :param crawler: Target crawler name
        :param implementation: Class that should implement the interface

        :type interface: Generic[InterfaceType]
        :type implementation: Generic[ConcreteObjType]
        :type crawler: str
        """

        self.Interface = interface
        self.Crawler = crawler
        self.Implementation = implementation
