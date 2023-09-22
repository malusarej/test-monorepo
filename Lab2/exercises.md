# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, good coding practice ensures that you can tell a function's basic purpose from the name like the encode function returns the string encoded to bytes. For user defined functions, the name of the function should describe either the purpose of the function or what the end result needed is or both. For example, a good name for a user-defined function that returns the area of a circle would be areaOfCircle rather than just area as it describes what the end result is going to be. So a good practice would be to use verbs + purpose of function

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A dictionary is an unordered collection of key-value pairs and it uses a hash-table or hash map data structure where keys are hashed to determine their storage location whereas list is a ordered collection of elements that is stored in an array like structure where the elements are stored in a contiguous block of memory. Dictonaries are used for fast lookups of values whereas list is used to store a sequence of items.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, list allows random access that is access to any element and using myList[7] would give you access to element at index 7.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

One of the pros can be that it leads to code versatility and helps the developer by not making them write a separate code for each data type and reduce development time. Another pro is that reduces code duplication. Some of the cons is reduced type safety and limited optimization.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Functions are all "verbs" that may be good as they describe their actions such as the post, get methods etc. They're well named because they concisely describe their functions and aren't performing multiple actions.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

- request() and resolves_redirects() have a lot of arguements

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

It's a special syntax used to collect any special keyword arguments that are not explicitly defined as parameters and allows you to pass a variable number of keyword arguments to a function. It might be good because it allows flexibility because it can accept any number of keyword arguments even if the number is not known and that is useful for providing customization options. It may be bad because it could lead to runtime errors because the function may not be built to handle certain arguments.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

It allows users to omit that argument when providing values for their use case and this leads increased flexibility and usage.It also helps avoid errors in case user misses out on providing a value. Arguments can be set to any data type apart from None like for example a method could have an arguement that is string or integer. It might be good to set an argument by some predetermined value because it allows developers to cater to a wide variety of use cases and provide sensible defaults.
