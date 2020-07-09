import unittest
import pathlib

from unittest.mock import patch
from tests.child_class_logging import ChildClassNotAbc, ChildClassILogging
from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.IDataRepository import IDataRepository
from sosi_crawler_interfaces.ILogging import ILogging
from object_factory.factory import ObjectFactory

FILE_PATH = pathlib.Path(__file__).parent.__str__()

class test_add_dependency(unittest.TestCase):
    def test_should_add_dependency_with_sucess(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            log_class: ILogging = type('log_class', (ILogging,), {})

            factory.AddDependency('test_should_add_dependency_with_sucess', ILogging, log_class)
            self.assertTrue(True)
        except ValueError as e:
            self.assertTrue(False, str(e))

    def test_should_not_add_dependency_error_duplicate(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            log_class: ILogging = type('log_class', (ILogging,), {})
            
            factory.AddDependency('test_should_not_add_dependency_error_duplicate', ILogging, log_class)
            factory.AddDependency('test_should_not_add_dependency_error_duplicate', ILogging, log_class)

            self.assertTrue(False)
        except Exception as e:
            self.assertRaises(ValueError)
            self.assertTrue(str(e).lower() == 'dependecy already set')

    def test_should_add_two_diff_dependencies_same_crawler(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            repo_class: IDataRepository = type('repo_class', (IDataRepository,), {})
            log_class: ILogging = type('log_class', (ILogging,), {})
            
            factory.AddDependency('test_should_add_two_diff_dependencies_same_crawler', IDataRepository, repo_class)
            factory.AddDependency('test_should_add_two_diff_dependencies_same_crawler', ILogging, log_class)

            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, str(e))

    def test_should_not_add_interface_not_subclass_abc(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.AddDependency('test_should_not_add_interface_not_subclass_abc', type("not_abc_base_class", (), {}), type("not_abc_class", (), {}))

            self.assertTrue(False)
        except Exception as e:
            self.assertRaises(TypeError)
            self.assertTrue(str(e).lower().__contains__('not subclass of'))

    def test_should_not_add_dependency_isnt_instance_interface(self):
        try:
            factory: IObjectFactory = ObjectFactory()

            factory.AddDependency('test_should_not_add_dependency_isnt_instance_interface', ILogging, factory)

            self.assertTrue(False)
        except Exception as e:
            self.assertRaises(TypeError)
            self.assertTrue(str(e).lower().__contains__('not subclass of'))

if __name__ == '__main__':
    unittest.main()
