# This class was writen, along with main.py, for the
# Capital One technical assessment.
#
# This class encapsulates all the logic behind the 
# source code file analysis.
#
# Please see main.py for a more detailed description
# of the functionality of this program.

class AnalyzeCode:
    """
    This class is to analyze source code files for statistics
    on commenting. This program was written for the Capital One
    technical assessment.

    Attributes:
        file_name (str): The source code file name
        supported_languages_file (str): The supported languages schema file name
        file_contents (list[str]): The individual lines of the source code
        file_extension (str): The file extension
        single_line_comment (str): The syntax for single line comments
        multi_line_comment (list[str]): The syntax for multi line comments
    """
    def __init__(self, file_name, supported_languages_file):
        """
        The constructor for the AnalyzeCode class.

        Parameters:
            file_name (string): The source code file name
            supported_languages_file (string): The supported languages schema file name
        """
        self.file_name = file_name
        self.supported_languages_file = supported_languages_file

    def parse_file(self):
        """
        Parses the source code file into individual lines, and determine
        commenting syntax
        """
        with open(self.supported_languages_file) as schema_file:
            file_lines = schema_file.readlines()
            for line in file_lines:
                schema = line.strip().split(',')
                # Check if file extension matches
                if schema[0] in self.file_name:
                    self.file_extension = schema[0]
                    self.single_line_comment = schema[1] if len(schema[1]) > 0 else None
                    self.multi_line_comment = schema[2:] if len(schema[2]) > 0 else None

        # If file extension can't be found in supported languages
        try:
            self.file_extension
        except:
            raise FileNotFoundError

        with open(self.file_name) as source_file:
            source_lines = source_file.readlines()
            self.file_contents = [line.strip() for line in source_lines]


    def total_lines(self):
        """
        Calculates the total number of lines of code and comments

        Returns:
            int: The total number of lines
        """
        return len(self.file_contents)

    def comment_lines(self):
        """
        Calculates the total number of comment lines

        Returns:
            int: The total number of comment lines
        """
        total_comments = 0
        multi_line = False # To account for lines enclosed in multi-line comments
        for line in self.file_contents:
            if self.multi_line_comment and self.multi_line_comment[0] in line and self.multi_line_comment[1] in line:
                # Single line comment
                total_comments += 1
            # Check for multi line comments 
            elif self.multi_line_comment and self.multi_line_comment[0] in line:
                multi_line = True
                total_comments += 1
            elif self.multi_line_comment and self.multi_line_comment[1] in line:
                multi_line = False
                total_comments += 1
            else:
                if self.single_line_comment and (multi_line or self.single_line_comment in line):
                    total_comments += 1
        return total_comments

    def single_line_comments(self):
        """
        Calculates the number of single line comments

        Returns:
            int: The total number of comment lines
        """
        if not self.single_line_comment:
            return 0
        total_comments = 0
        for line in self.file_contents:
            # Check for single-line comments
            if self.single_line_comment in line:
                total_comments += 1
        return total_comments

    def comments_in_blocks(self):
        """
        Calculates the number of comment lines in block comments

        Returns:
            int: The total number of comment lines
        """
        return self.comment_lines() - self.single_line_comments()
    def block_comments(self):
        """
        Calculates the number of block comments

        Assume that single line block comments qualify: e.g. /*...*/ 

        Returns:
            int: The total number of block comments
        """
        if not self.multi_line_comment:
            return 0
        total_comments = 0
        multi_line = False # To account for lines enclosed in multi-line comments
        for line in self.file_contents:
            # Check for multi-line comments
            if self.multi_line_comment[0] in line:
                multi_line = True
            # Not elif to account for single lines
            if self.multi_line_comment[1] in line and multi_line:
                multi_line = False
                total_comments += 1
        return total_comments

    def count_todos(self):
        """
        Calculates the number of TODO's

        Returns:
            int: The total number of TODO's
        """
        total_todos = 0
        for line in self.file_contents:
            if 'TODO' in line:
                total_todos += 1
        return total_todos
