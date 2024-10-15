import unittest
from unittest.mock import MagicMock
from ProgramHooks.hook_manager import HookManager

class TestHookManager(unittest.TestCase):
    def setUp(self):
        """Set up the HookManager instance for testing."""
        self.hook_manager = HookManager()

    def test_default_stages(self):
        """Test that HookManager initializes with default stages."""
        expected_stages = ['pre_init', 'post_init', 'pre_runtime', 'post_runtime']
        self.assertListEqual(list(self.hook_manager.hooks.keys()), expected_stages)

    def test_register_hook(self):
        """Test that a hook can be registered and logged correctly."""
        mock_func = MagicMock(name="mock_func")
        self.hook_manager.register_hook('pre_init', mock_func)
        self.assertIn(mock_func, self.hook_manager.hooks['pre_init'])

    def test_execute_hooks(self):
        """Test executing hooks with arguments."""
        mock_func = MagicMock(name="mock_func")
        self.hook_manager.register_hook('pre_runtime', mock_func)
        
        self.hook_manager.execute_hooks('pre_runtime', 42, key='value')
        
        # Ensure that the hook was called with the correct arguments
        mock_func.assert_called_with(42, key='value')

    def test_execute_hooks_invalid_stage(self):
        """Test executing hooks for an invalid stage should log an error."""
        with self.assertLogs('HookManager', level='CRITICAL') as log:
            self.hook_manager.execute_hooks('invalid_stage')
            self.assertIn('Unexpected Program Error: Invalid stage provided', log.output[0])

    def test_no_hooks_for_stage(self):
        """Test that warning is logged when no hooks are found for a stage."""
        with self.assertLogs('HookManager', level='WARNING') as log:
            self.hook_manager.execute_hooks('post_runtime')
            self.assertIn('No hooks found for stage: post_runtime', log.output[0])

    def test_load_plugins(self):
        """Test loading plugins from a folder."""
        # This test will mock the load_plugins method behavior without needing actual files.
        with unittest.mock.patch('mypackage.hookmanager.glob.glob', return_value=['plugin1.py']):
            with unittest.mock.patch('mypackage.hookmanager.importlib.import_module') as mock_import:
                mock_module = MagicMock()
                mock_import.return_value = mock_module

                self.hook_manager.load_plugins('/some/fake/folder')

                # Ensure the import was attempted on the correct module
                mock_import.assert_called_with('plugin1')
    
    def test_register_module_hooks(self):
        """Test registering hooks from a module."""
        mock_module = MagicMock()
        mock_func = MagicMock()
        mock_module.pre_init = mock_func

        self.hook_manager._register_module_hooks(mock_module)

        # Ensure the pre_init hook was registered
        self.assertIn(mock_func, self.hook_manager.hooks['pre_init'])

if __name__ == "__main__":
    unittest.main()
