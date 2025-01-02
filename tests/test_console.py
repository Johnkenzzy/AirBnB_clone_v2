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
            self.assertIn("Exits the program without formatting", mock_stdout.getvalue())

    def test_do_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    def test_do_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

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
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    def test_do_show_invalid_class(self):
        """Test show with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show InvalidClass")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    def test_do_show_missing_id(self):
        """Test show with missing ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    def test_do_show_no_instance_found(self):
        """Test show with non-existing instance ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel 1234")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    def test_do_all_invalid_class(self):
        """Test all with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all InvalidClass")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    def test_do_all_valid_class(self):
        """Test all with valid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
             patch('models.storage._FileStorage__objects', {"BaseModel.1234": "[BaseModel]"}):
            self.console.onecmd("all BaseModel")
            self.assertIn("[BaseModel]", mock_stdout.getvalue())

    @unittest.skip("Skip to test later")
    def test_do_destroy_missing_class(self):
        """Test destroy with missing class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    def test_do_destroy_invalid_class(self):
        """Test destroy with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy InvalidClass")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    def test_do_destroy_missing_id(self):
        """Test destroy with missing ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    def test_do_destroy_no_instance_found(self):
        """Test destroy with non-existing instance ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel 1234")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")


if __name__ == "__main__":
    unittest.main()
