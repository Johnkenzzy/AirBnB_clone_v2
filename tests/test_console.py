"""
Unittest for HBNB console commands
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand console"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def test_prompt(self):
        """Test the prompt"""
        self.assertEqual(self.console.prompt, "(hbnb) ")

    def test_emptyline(self):
        """Test the emptyline method does nothing"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("")
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_do_quit(self):
        """Test quit command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_do_EOF(self):
        """Test EOF command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_help_quit(self):
        """Test help for quit command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help quit")
            self.assertIn("Exits the program", mock_stdout.getvalue())

    def test_help_EOF(self):
        """Test help for EOF command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help EOF")
            msg = "Exits the program without formatting"
            self.assertIn(msg, mock_stdout.getvalue())

    def test_do_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create")
            err_msg = "** class name missing **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create InvalidClass")
            err_mgs = "** class doesn't exist **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_mgs)

    def test_do_create_valid_class(self):
        """Test create with a valid class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
                patch('models.storage.save', MagicMock()):
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Check if an ID is printed

    def test_do_show_missing_class(self):
        """Test show with missing class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show")
            err_msg = "** class name missing **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_show_invalid_class(self):
        """Test show with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show InvalidClass")
            err_msg = "** class doesn't exist **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_show_missing_id(self):
        """Test show with missing ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            err_msg = "** instance id missing **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_show_no_instance_found(self):
        """Test show with non-existing instance ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel 1234")
            err_msg = "** no instance found **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_all_invalid_class(self):
        """Test all with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all InvalidClass")
            err_msg = "** class doesn't exist **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_all_valid_class(self):
        """Test the 'all' command with a valid class name."""
        mock_objects = {
            "BaseModel.1234": "[BaseModel](1234) {
                'id': '1234', 'name': 'Test'}",
            "BaseModel.5678": "[BaseModel](5678) {
                'id': '5678', 'name': 'Another Test'}"
        }
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, patch(
                'models.storage.all', return_value=mock_objects):
            self.console.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()

            # Assert expected output
            self.assertIn("[BaseModel](1234)", output)
            self.assertIn("[BaseModel](5678)", output)
            self.assertNotIn("AnotherModel", output)

    @unittest.skip("Not applicable")
    def test_do_all_valid_class(self):
        """Test all with valid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, patch(
                'models.storage._FileStorage__objects', {
                        "BaseModel.1234": "[BaseModel]"}):
            self.console.onecmd("all BaseModel")
            self.assertIn("[BaseModel]", mock_stdout.getvalue())

    @unittest.skip("Skip to test later")
    def test_do_destroy_missing_class(self):
        """Test destroy with missing class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy")
            err_msg = "** class name missing **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_destroy_invalid_class(self):
        """Test destroy with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy InvalidClass")
            err_msg = "** class doesn't exist **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_destroy_missing_id(self):
        """Test destroy with missing ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            err_msg = "** instance id missing **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)

    def test_do_destroy_no_instance_found(self):
        """Test destroy with non-existing instance ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel 1234")
            err_msg = "** no instance found **"
            self.assertEqual(mock_stdout.getvalue().strip(), err_msg)


if __name__ == "__main__":
    unittest.main()
