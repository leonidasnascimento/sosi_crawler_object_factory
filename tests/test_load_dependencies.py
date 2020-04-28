import unittest
from unittest.mock import patch

from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.ILogging import ILogging
from object_factory.ObjectFactory import ObjectFactory

class test_load_dependencies(unittest.TestCase):
    def test_should_load_from_file_sucessfully(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies("tests\\dependencies.json")
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass        
        pass
    
    def test_should_not_load_from_empty_param(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies("")

            repoFromGetInstance: ILogging = factory.GetInstance("test", ILogging)
            self.assertTrue(repoFromGetInstance is None)
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass        
        pass

    def test_should_not_load_from_file_notfound(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies("tests\\dependencies__.json")
            
            self.assertTrue(False)
            pass
        except Exception:
            self.assertRaises(FileNotFoundError)
            pass        
        pass
    
    def test_should_not_load_param_interface_missing(self):        
        pass
    
    def test_should_not_load_param_implementation_missing(self):        
        pass
    
    def test_should_not_load_param_crawler_missing(self):        
        pass
    pass