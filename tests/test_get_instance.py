import unittest
from unittest.mock import patch

from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.IDataRepository import IDataRepository
from object_factory.ObjectFactory import ObjectFactory

class test_get_instance(unittest.TestCase):
    def test_should_get_instance_from_added_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            repo: IDataRepository = unittest.mock.MagicMock(spec=IDataRepository)

            factory.AddDependency("test_should_get_instance_from_added_dependency", IDataRepository, repo)
            repoFromGetInstance = factory.GetInstance("test_should_get_instance_from_added_dependency", IDataRepository)

            self.assertTrue(isinstance(repoFromGetInstance, unittest.mock.MagicMock))
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass        
        pass

    def test_should_get_instance_from_loaded_predefined_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies("tests/dependencies.json")

            repoFromGetInstance = factory.GetInstance("test", IDataRepository)

            self.assertTrue(isinstance(repoFromGetInstance, unittest.mock.MagicMock))
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass        
        pass

    def test_should_not_get_instance_from_unknown_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            repo: IDataRepository = unittest.mock.MagicMock(spec=IDataRepository)

            factory.AddDependency("test_should_get_instance_from_added_dependency", IDataRepository, repo)
            repoFromGetInstance = factory.GetInstance("test", IDataRepository)

            self.assertTrue(repoFromGetInstance is None)
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass        
        pass
    pass

if __name__ == '__main__':
    unittest.main()