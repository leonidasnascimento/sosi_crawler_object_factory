import unittest
from unittest.mock import patch
from unit_tests.child_class_logging import ChildClassNotAbc
from sosi_crawler_interfaces.IObjectFactory import IObjectFactory
from sosi_crawler_interfaces.IDataRepository import IDataRepository
from sosi_crawler_interfaces.ILogging import ILogging
from object_factory.factory import ObjectFactory

class test_add_dependency(unittest.TestCase):
    def test_should_add_dependency_with_sucess(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            patcher: unittest.mock.patch = unittest.mock.patch.object(unittest.mock.MagicMock, '__bases__', (IDataRepository,))

            with patcher:
                patcher.is_local = True

                factory.AddDependency('test_should_add_dependency_with_sucess', IDataRepository, unittest.mock.MagicMock)

            self.assertTrue(True)
            pass
        except ValueError as e:
            self.assertTrue(False, str(e))
            pass
        pass

    def test_should_not_add_dependency_error_duplicate(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            patcher: unittest.mock.patch = unittest.mock.patch.object(unittest.mock.MagicMock, '__bases__', (IDataRepository,))

            with patcher:
                patcher.is_local = True

                factory.AddDependency('test_should_not_add_dependency_error_duplicate', IDataRepository, unittest.mock.MagicMock)
                factory.AddDependency('test_should_not_add_dependency_error_duplicate', IDataRepository, unittest.mock.MagicMock)

            self.assertTrue(False)
            pass
        except Exception as e:
            self.assertRaises(ValueError)
            self.assertTrue(str(e).lower() == 'dependecy already set')
            pass
        pass

    def test_should_add_two_diff_dependencies_same_crawler(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            patchRepo: unittest.mock.patch = unittest.mock.patch.object(unittest.mock.MagicMock, '__bases__', (IDataRepository,))
            patchLog: unittest.mock.patch = unittest.mock.patch.object(unittest.mock.MagicMock, '__bases__', (ILogging,))

            with patchRepo, patchLog:
                patchRepo.is_local = True
                patchLog.is_local = True

                factory.AddDependency('test_should_add_two_diff_dependencies_same_crawler', IDataRepository, unittest.mock.MagicMock)
                factory.AddDependency('test_should_add_two_diff_dependencies_same_crawler', ILogging, unittest.mock.MagicMock)

            self.assertTrue(True)
            pass
        except Exception as e:
            self.assertTrue(False, str(e))
            pass
        pass

    def test_should_not_add_interface_not_subclass_abc(self):
        try:
            factory: IObjectFactory = ObjectFactory()
            factory.AddDependency('test_should_not_add_interface_not_subclass_abc', ChildClassNotAbc, unittest.mock.MagicMock)

            self.assertTrue(False)
            pass
        except Exception as e:
            self.assertRaises(TypeError)
            self.assertTrue(str(e).lower().__contains__('not subclass of'))
            pass
        pass

    def test_should_not_add_dependency_isnt_instance_interface(self):
        try:
            factory: IObjectFactory = ObjectFactory()

            factory.AddDependency('test_should_not_add_dependency_isnt_instance_interface', ILogging, factory)

            self.assertTrue(False)
        except Exception as e:
            self.assertRaises(TypeError)
            self.assertTrue(str(e).lower().__contains__('not subclass of'))
            pass
        pass
    pass

if __name__ == '__main__':
    unittest.main()
