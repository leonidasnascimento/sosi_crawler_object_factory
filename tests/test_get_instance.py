import unittest
import pathlib
from unittest.mock import patch

from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.IDataRepository import IDataRepository
from sosi_crawler_interfaces.ILogging import ILogging
from object_factory.factory import ObjectFactory

FILE_PATH = pathlib.Path(__file__).parent.__str__()

class test_get_instance(unittest.TestCase):
    def test_should_get_instance_from_added_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            patcher: unittest.mock.patch = unittest.mock.patch.object(unittest.mock.MagicMock, '__bases__', (IDataRepository,))

            with patcher:
                patcher.is_local = True

                factory.AddDependency('test_should_get_instance_from_added_dependency', IDataRepository, unittest.mock.MagicMock)
                repoFromGetInstance = factory.GetInstance('test_should_get_instance_from_added_dependency', IDataRepository)

                self.assertTrue(isinstance(repoFromGetInstance, IDataRepository))
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass
        pass

    def test_should_get_instance_from_loaded_predefined_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.LoadDependencies(FILE_PATH + '/dependencies.json')

            repoFromGetInstance: ILogging = factory.GetInstance('test', ILogging)
            self.assertTrue(isinstance(repoFromGetInstance, ILogging))

            repoFromGetInstance.Log('Hello World!')
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass
        pass

    def test_should_not_get_instance_from_unknown_dependency(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            patcher: unittest.mock.patch = unittest.mock.patch.object(unittest.mock.MagicMock, '__bases__', (IDataRepository,))

            with patcher:
                patcher.is_local = True

                factory.AddDependency('test_should_get_instance_from_added_dependency', IDataRepository, unittest.mock.MagicMock)
                repoFromGetInstance = factory.GetInstance('test', IDataRepository)

            self.assertTrue(repoFromGetInstance is None)
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass
        pass
    pass

if __name__ == '__main__':
    unittest.main()
