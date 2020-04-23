import unittest
from unittest.mock import patch

from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.IDataRepository import IDataRepository
from sosi_crawler_interfaces.ILogging import ILogging
from object_factory.ObjectFactory import ObjectFactory

class test_add_dependency(unittest.TestCase):
    def test_should_add_dependency_with_sucess(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            repo: IDataRepository = unittest.mock.MagicMock(spec=IDataRepository)

            factory.AddDependency("test_should_add_dependency_with_sucess", IDataRepository, repo)
            
            self.assertTrue(True)
            pass
        except ValueError as e:
            self.assertTrue(False, str(e))
            pass        
        pass

    def test_should_not_add_dependency_error_duplicate(self):
        try:
            factory: IObjectFactory = ObjectFactory()            
            repo: IDataRepository = unittest.mock.MagicMock(spec=IDataRepository)

            factory.AddDependency("test_should_not_add_dependency_error_duplicate", IDataRepository, repo)
            factory.AddDependency("test_should_not_add_dependency_error_duplicate", IDataRepository, repo)

            self.assertTrue(False)
            pass
        except Exception as e:
            self.assertRaises(ValueError)
            self.assertTrue(str(e).lower() == "dependecy already set")
            pass        
        pass

    def test_should_add_two_diff_dependencies_same_crawler(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            repo: IDataRepository = unittest.mock.MagicMock(spec=IDataRepository)
            log: ILogging = unittest.mock.MagicMock(spec=ILogging)

            factory.AddDependency("test_should_add_two_diff_dependencies_same_crawler", IDataRepository, repo)
            factory.AddDependency("test_should_add_two_diff_dependencies_same_crawler", ILogging, log)

            self.assertTrue(True)
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass        
        pass
    pass

if __name__ == '__main__':
    unittest.main()