import unittest
import pathlib

from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.IDataRepository import IDataRepository
from sosi_crawler_interfaces.ILogging import ILogging
from sosi_crawler_object_factory.factory import ObjectFactory
from tests.child_class_logging import ChildClassILogging 

FILE_PATH = pathlib.Path(__file__).parent.__str__()

class test_get_instance(unittest.TestCase):
    def test_should_get_instance_from_added_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()

            factory.AddDependency('test_should_get_instance_from_added_dependency', ILogging, ChildClassILogging)
            
            repo_from_get_instance = factory.GetInstance('test_should_get_instance_from_added_dependency', ILogging)

            self.assertTrue(isinstance(repo_from_get_instance, ILogging))
        except Exception as e:
            self.assertTrue(False, str(e))

    def test_should_get_instance_from_loaded_predefined_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies(FILE_PATH + '/dependencies.json')

            repo_from_get_instance: ILogging = factory.GetInstance('test', ILogging)
            self.assertTrue(isinstance(repo_from_get_instance, ILogging))

            repo_from_get_instance.Log('Hello World!')
        except Exception as e:
            self.assertTrue(False, str(e))

    def test_should_not_get_instance_from_unknown_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            log_class: ILogging = type('log_class', (ILogging,), {})

            factory.AddDependency('test_should_add_dependency_with_sucess', ILogging, log_class)
            repo_from_get_instance = factory.GetInstance('test', ILogging)

            self.assertTrue(repo_from_get_instance is None)
        except Exception as e:
            self.assertTrue(False, str(e))

if __name__ == '__main__':
    unittest.main()
