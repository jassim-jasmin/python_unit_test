"# python_unit_test" 

Function main method `py_unit_test.py`

1. Apply decorator function to the testing function
2. Decorator has 3 functionality
    1. Registering the test case
    2. Applying the unit test
    3. Perform the function action
   
### Outuput
1. New directory will be created in the same working directory as main file execution.
2. Name of the directory will be argument pass to the constructor UnitTest
3. For each test two json file will be created,
   1. test_`main executing file name`_`testing function name`.json
   2. missmatch_test_`main executing file name`_`testing function name`.json
   

Refer `doc/` directory for more details about this project

Try:

Windows
-
       python main.py --help
   
Ubuntu
-
      python3 main.py --help

Example
-
      (for windows): python main.py -test

      (for ubuntu): python3 main.py -test