import unittest
import pathlib

from unittest.mock import patch
from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.ILogging import ILogging
from object_factory.factory import ObjectFactory

FILE_PATH = pathlib.Path(__file__).parent.__str__()

class test_load_dependencies(unittest.TestCase):
    def test_should_load_from_file_sucessfully(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies(FILE_PATH + '\\dependencies.json')
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass
        pass

    def test_should_not_load_from_empty_json_file_param(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies('')

            repoFromGetInstance: ILogging = factory.GetInstance('test', ILogging)
            self.assertTrue(repoFromGetInstance is None)
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass
        pass

    def test_should_not_load_from_file_notfound(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies(FILE_PATH + '\\dependencies__.json')

            self.assertTrue(False)
            pass
        except Exception:
            self.assertRaises(FileNotFoundError)
            pass
        pass

    def test_should_not_load_param_interface_missing(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies(FILE_PATH + '\\dependencies_no_interface.json')

            self.assertTrue(False)
            pass
        except Exception as e:
            self.assertRaises(AttributeError)
            self.assertTrue(str(e).__contains__('interface'))
            pass
        pass

    def test_should_not_load_param_implementation_missing(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies(FILE_PATH + '\\dependencies_no_implementation.json')

            self.assertTrue(False)
            pass
        except Exception as e:
            self.assertRaises(AttributeError)
            self.assertTrue(str(e).__contains__('implementation'))
            pass
        pass

    def test_should_not_load_param_crawler_missing(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies(FILE_PATH + '\\dependencies_no_crawler.json')

            self.assertTrue(False)
            pass
        except Exception as e:
            self.assertRaises(AttributeError)
            self.assertTrue(str(e).__contains__('crawler'))
            pass
        pass
    pass
