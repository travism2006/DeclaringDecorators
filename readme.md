# Declaring Decorators

Common tasks like write to a log file (aka logging) is done by using decorators. Some obvious cases for writing
decorators include:

* log function call or metadata to file
* find execution time
* DB transactions
* authentication requirements
* parsing arguments (cleaning/pre-processing inputs)

## Installation

**(note: the software is not pip ready/configured yet)**
Use "pip install decdec" to get the module, and you can start doing new tricks with decorators.

## As of
30 August 2021
 * v1.0.2 started
   * Completed features
     * decIter
       * returns an iterable from a function or decorator
       * **Use Case**: see source code definition for the func. or decorator
   * Features in progress
     * decScan - 
     * customizable template decorators
     * customizable decorators
     * standard boilerplate decorators (e.g. logging, validation, authentication, etc.)

## Future features
 * find basic stats on a file or list of files for all decorators (and decorator templates)
 * can list decorators and iterate over them
 * create your own custom iterable to go over a list of decorators
 * support new syntax for combining the application of multiple decorators
   * add 2 decorators, non-exclusive: logWarnings + printTextMenu
   * add 2, excluding common data:  logWarnings ~ printTextMenu
   * subtract _(maybe using lambda or map or list comprehension)_: log2All - (query string to filter out of results)
   * 