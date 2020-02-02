# Capital One Technical Assessment 
# Created by Jason Guo
#
# This program, alongside the AnalyzeCode class, was my interpretation of
# the Capital One technical assessment.
#
# In the context of automation and continuous deployment, this program
# was written to take in the source code files as command-line arguments.
# You may supply in an arbitrary number of source code files as arguments,
# in the form of file paths.
#
# In the spirit of modularity, I've added a 'programming languages schema', 
# which defines the programming language and its commenting syntax. This program
# is thus easily scalable to allow for different programming languages.
#
# The format is:
#       file_extension,single_line_comment,begin_multi_line_comment,end_multi_line_comment
# e.g.  .java,//,/*,*/
#
# (See supported_languages.csv as an example)
#
# To run the program:
# python main.py [source code file names] schema_file
#
# An example command would be:
# python main.py sample.html sample.java sample.js sample.js supported_languages.csv


# For command-line arguments
import argparse
from AnalyzeCode import AnalyzeCode

# Instantiate argument parser
parser = argparse.ArgumentParser(description='Analyze some source files')
parser.add_argument('file_names', metavar='file_name', type=str, nargs='*', help='the file names of the source code files')
parser.add_argument('supported_languages', metavar='comment_schema', type=str, help='the supported programming languages and their commenting syntax')

args = parser.parse_args()

# Check for valid supported languages file
try:
    open(args.supported_languages)
except:
    print("Invalid supported languages schema file")
    quit()

# Process each source code file
for file_name in args.file_names:
    print(f'##### {file_name.upper()} #####')
    
    # Instantiate AnalyzeCode object for code parsing
    analyzer = AnalyzeCode(file_name, args.supported_languages)
    
    try:
        analyzer.parse_file()
    except:
        # If either the file can't be found, or if it's not defined in the supported languages
        print("Invalid source file\n")
        continue

    # Output
    print(f'Total # of lines: {analyzer.total_lines()}')
    print(f'Total # of comment lines: {analyzer.comment_lines()}')
    print(f'Total # of single line comments: {analyzer.single_line_comments()}')
    print(f'Total # of comment lines within within block comments: {analyzer.comments_in_blocks()}')
    print(f'Total # of block line comments: {analyzer.block_comments()}')
    print(f'Total # of TODO\'s: {analyzer.count_todos()}\n')
