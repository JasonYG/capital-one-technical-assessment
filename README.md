# Capital One Technical Assessment 
#### Created by Jason Guo

The main.py and AnalyzeCode.py program files were my interpretation of
the Capital One technical assessment.

# To run the program:
`python main.py [source code file names] schema_file`

An example command would be:  
`python main.py sample.html sample.java sample.js sample.js supported_languages.csv`

# Rationale
In the context of automation and continuous deployment, this program
was written to take in the source code files as command-line arguments.
You may supply in an arbitrary number of source code files as arguments,
in the form of file paths.

In the spirit of modularity, I've added a 'programming languages schema', 
which defines the programming language and its commenting syntax. This program
is thus easily scalable to allow for different programming languages.

The format is:  
      `file_extension,single_line_comment,begin_multi_line_comment,end_multi_line_comment`    
e.g.  `.java,//,/*,*/`

(See supported_languages.csv as an example)

# Assumptions
1. Source code files have the appropriate file extension (e.g. Python files have the .py extension)
2. The programming language has a unique way to create single line and multi-line comments (e.g. '//' is the only way to define a single-line comment in Java, '/*' and '*/' is the only way to define a multi-line comment in Java)
3. There is a correctly formatted schema file (see above and supported_languages.csv)
4. Multi-line comments that only span a single line count as a multi-line comment

