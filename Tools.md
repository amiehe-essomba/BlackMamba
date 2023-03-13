# Classes

To create a class, it must have a name and the choice of the name of a class is not random, it must respect a certain number of criteria: it must start with an upper or lower case letter, it cannot contain only alphabetic characters and the underscore character, its length does not matter. The creation of a __class__ is done using the keyword **class** followed by the name of the class and ends with a **:** to indicate the end of the chain, its closure is done using the keyword **end** followed by **:** 
**A class can only contain classes and functions, but also attributes and methods. Attributes are variables that belong to the class or its instances, while methods are functions defined within the class that operate on its instances, nothing else.**

## Creating a class
- **Using a constructor method named __initialize()__ function to make variables global**

```ruby
class iris:
    def initialize() -> None
        self.color  = 'green'
        self.length = 1.5
        self.width  = 0.3
    end:
end:
```

The constructor method initializes  attributes with  values passed as parameters.

- **Defining default values inside a constructor method named __initialize()__**

```ruby
class iris:
    def initialize( color : string = "green") -> None:
        self.color  = color
        self.length = 1.5
        self.width  = 0.3
    end:
end:
```

The **initialize()** function returning no value its output is always defined on **None**.
It is also possible to define some variables in this function to make them more accessible in all functions connected to the host class, so no need to create several variables for each function. These variables created in the **initialize()** function are called **semi-global** because they can be accessed from any method within the class. By initializing these variables in the constructor method,
you can ensure that they are available throughout the class without having to redefine them in each method. In Black Mamba, you can define semi-global variables in the initialize() method like this:
To create a pure global variable it is necessary to use the **global** function (see later), these variables are not only accessible in all classes, and functions(methods) they can be used throughout the code it's up to you to decide which statement works best for you.
In the constructor method **initialize()** you can also define default values as illustrated above.
The use of this constructor method is really very practical and very useful, however if it is created, it must be the first to appear in a class because it is an initialization function and cannot be called in the code or even the entire program.


```ruby
class iris:
    def initialize() -> None:
        self.color  = 'green'     # sheets color
        self.size   = 1.2         # its size
        self.width  = 0.3         # sheets width
    end:
    
    # get items
    def get( item : string ) -> dictionary:
        return {color : color, size: size, width : width}
    end:
end:    

print * iris().get()
```


## Inheritance classes

```ruby
class setosa:
    def initialize( color : string = 'red', size : float) -> None:
        self.color = color
        self.size  = size 
        self.width = 0.3
    end:
end:

class iris( setosa ):
    def get():
        return {color : color, size : size, width : width}
    end:
end:

print * iris.get(), iris.color, iris.size, iris.width
```

Inheritance is a powerful feature in object-oriented programming that allows you to create a new class based on an existing class. The new class, known as the subclass or derived class, inherits the properties and methods of the existing class, known as the superclass or base class, and can also add its own properties and methods or modify those inherited from the base class.
We start by creating a class setosa containing only the semi-global variables of this class using constructor method just to simplify things then a second class is created ( host class ), the class iris will host the class setosa just by defining setosa between brackets and so iris can access all of setosa's information down to the smallest detail.
In this example, **setosa** is the base class and **iris** is the derived class. **iris** inherits the some function() method from **setosa**, but overrides it with its own implementation.
Another advantage of the base class is that it can access all the information of the derived class without modifying it. This means that the base class can use the properties and methods of the derived class, but without affecting its internal state.
This is particularly useful in scenarios where you need to perform operations on the derived class, but you don't want to modify its internal state. For example, if you have a base __class Animal__ and a derived __class Dog__, the base class can use the **bark()** method of the derived class to produce a **sound**, but it does not modify the state instance variable of the **Dog class**.
In other words, the base class can use the functionality of the derived class without disrupting its internal state. This is possible thanks to the notion of encapsulation, which allows to control access to the properties and methods of a class.


## Multiple inheritances

Multiple Inheritance is a feature in **Black Mama** programming language that allows a class to
inherit properties and methods from multiple parent classes. This means that a derived
class can have multiple base classes, and it can inherit their attributes and behaviors.
To define a class with multiple inheritance, we simply list the parent classes separated by commas in the class definition. For example

In this example, the class Derived inherits from both **setosa** and **versicolor**. This means that Derived has access to the methods me**get()** and **attributes of the constructor method** from its base classes.

Multiple inheritance can be very powerful, but it can also lead to some design
complexities and potential conflicts between the base classes. Therefore, it's important
to use multiple inheritance with caution and to ensure that the class hierarchy is well-designed and easy to understand



```ruby
class setosa:
    def initialize( color : string = 'red', size : float) -> None:
        self.color = color
        self.size  = size 
        self.width = 0.3
    end:
end:

class versicolor( setosa ):
    def get( item : string = 'color') -> string:
        if item == 'color':
            return color
        elif item == 'size':
            return length
        else:
            return 'item Error'
        end:
    end:
end:

class iris( setosa, versicolor ):
    def info( item : string = 'length' ) -> dictionary:
        # itialazing versicolor
        set = versicolor.get( item = item )
        return {color : color, size : size, width : width}
    end:
end:

print * iris.info( item = 'color'), iris.get(), iris.color 
```

## Multidimensional classes(nested classes or inner classes)

```ruby
class math:
    def initilaize( a : int = 0) -> None:
        self.a = a
    end:
    
    # creating a nested class or inner classs
    class arithmetic:
        def initialize( value : int ) -> None:
            self.value = value
        end:
        
        #creatng nested method fuunction
        def mean( c : float) -> float:
            return (a+b+c)/3.0
        end:
    end:
end:

print * math(a = 4).arithmetic(b = -4 ).sum(c = 2.0)
```

In this example, HostClass contains a nested class called **arithmethic**. arithmetic has its own __initialize()__ method 
that takes a value argument and sets an instance variable. math(host class) also has its own __initialize()__ method that 
creates an instance of arithmetic and assigns it to an instance variable called nested_object.

# Functions 
There are two different methods for creating functions: the first method uses the keyword **def** generally used for creating functions in a class but can be used globally, the second method uses the keyword **func** but cannot be used to create a function in a class only used outside of classes.
Just like classes, functions need a name the characteristics are identical (read the **Classes** section), a function can contain everything except classes which host functions.

## Function types.
It is possible to specify the type of a function using the keywords below:

- [x] None or none : No output
- [x] integer 
- [x] float 
- [x] boolean
- [x] string
- [x] complex
- [x] range
- [x] list
- [x] tuple
- [x] dictionary
- [x] ndarray
- [x] any
- [x] table

The default value is **any** it means that the output can be any type.
The type of a function is defined as follows:

```ruby
prod = func() -> list:
prod = func() -> tuple:
prod = func() -> any:
```

## Variable types defined in a function.

- [x] none for **None** type
- [x] int  for **integer** type
- [x] float for **float** type
- [x] bool for **boolean** type
- [x] string for **string** type
- [x] cplx for **complex** type
- [x] range for **range** type
- [x] list for **list** type
- [x] tuple for tuple **type**
- [x] dict for **dictionary** type
- [x] ndarray for **ndarray** type
- [x] table fot **table** type

A variable can have more than one type

```ruby
def prod( a : bool) -> float:
def prod( a : tuple list) -> integer:
def prod( a : float = 5.0) -> None:
```

## Creating a function using **def** as a keyword
```ruby
def Sum() -> float:
    list_of_values = [].random(10)
    return sum( list_of_values )
end:

print * Sum()
```

### Defining default values

```ruby
def index( id = 2 ) -> integer:
    list_of_values = [].random(10)
    return list_of_values.choice( id )
end:

print * index(id = 4)
```

```ruby
def List( id : int float, max : int = 5 ) -> list:
    list_of_values = [].random( id )
    return list_of_values[:max]
end:

print * List( id = 50 )
```

## Creating a function using **func** as a keyword
```ruby
Sum = func() -> float:
    list_of_values = [].random((10, (100,300)))
    return sum( list_of_values )
end:

print * Sum()
```


## Multidimensional functions(nested or inner functions)

```ruby
prod = func( a : float,  b : int) -> integer:
    # Floor is a nested or inner function 
    def Floor():
        str = string( a )
        str_int = integer( str.split('.')[ 0 ] )

        return str_int
    end:

    return Floor() * b
end:
```

# Module importations.
## Loading modules from the Library(Lib) or the Current Working Directory(CWD).

```ruby
1. from module matrix load ndarray

List = [1, 2, 3, 4]
ndarray(List, 2, 2).array(reverse = True, axis = None) 

2. load module matrix 

maxtrix.ndarray(List, 2, 2).array(reverse = True, axis = None) 
```

### Multiple-Importations 

```ruby
1. from module maths load statistics, trigo

List = [1, 2, 3, 4]
MEAN = statistics.mean( List)
PI   = trigo.pi

2. load module maths, physics

Bohr_radus = physics.B_radius
```

### Creating an alias.
```ruby
1. from module matrix load ndarray as nd

List = [1, 2, 3, 4]
nd(List, 2, 2).array(reverse = True, axis = None) 

2. load module matrix as mt

mt.ndarray(List, 2, 2).array(reverse = True, axis = None) 
```

### Loading all modules.
```ruby
1. from module matrix load *

List = [1, 2, 3, 4]
List_arr = ndarray(List, 2, 2).array() 
List_std = ndarray(List, 2, 2).std() 

2. from module prompt load *

prompt(List_arr, List_std)
```
## Loading modules from specific directory.

```ruby
1. from module /path/matrix/ load mode
2. from module /path/matrix/ load mode as md
3. from module /path/matrix/ load *
4. load module /path/matrix/
6. load module /path/matrix/ as mx

path is the module location
matrix is the modules's name 
```

# Handling files(open, read, write) 
## Opening a file.

For opening a new file, we can use the keyword **open** as defined bellow.

```ruby
open(name, file, action, status, encoding, error)
```

- [ ] **name** is an alias connected to the opening file 
- [ ] **file** is the file name or location+file name
- [ ] **action** could be **r** for reading, **w** for writing or **rw** for reading and writing
- [ ] **status** specifies if that is a old or new opening file. It could be **new** for new file or **old** respectively
- [ ] **encoding** could take these value [utf-8, ascii, utf-16, utf-32, latin-1, cp1252] 
- [ ] **error** takes only **surrogateescape** value, It is a default value

```
open(name=my_file, file='BlackMamba/README.md/, action='r', status='old', encoding='ascii' )
```

## Reading the opening file(Existing file).

For reading the opening file we can use to keywords **readline** for specific line and **readlines** for entire file. 

```ruby
name of the opening file = my_file (see sec. above )

1. my_file.readline(n=line)
reading a specific line 

2. my_file.readlines()
reading entire opening file until EOF.
```
[ ] **n** is a specific line in the opening file.

## Closing the opening file

For closing the opening file we can just use the keyword **close** as it is defined bellow. 

```ruby
name of the opening file = my_file

my_file.close()
```

## Using the keyword >with< 

Usually for reading or writing directly in the opening file. It's **faster** and **easier**.

```ruby:
with open(name=my_file, file='BlackMamba/README.md/, action='r', status='old', encoding='ascii' ):
    my_file.readlines()
end:
```

# Get user inputs 
## Using the sget function 

```ruby
sget( input, sep, char)

```
- [ ] **input** is a character we set at the beginning of the string( always a string type )
- [ ] **sep** is a separator, if sep is not None the output is a list due to the **split()** function (string or None type) 
- [ ] **char** is a boolean type set on True if we only need a char or False if we need a string  

> Example

```ruby
sget(input=">>>", sep = ".", char=False)
```

## Using scan function from input module
```ruby

from module input load scan 

scan(input, termios, fg, blink, hide )
```
- [ ] **input** is the same as in sget 
- [ ] **termios** is the inner IDE we want to use, curently version of BM only has two types of termios : **pegasus** the simplest one and **orion** the must permorming one with syntaxic coloration.
- [ ] **fg** is the color of the string input, you can fine the database color below.
- [ ] **blink** is a boolean type, if we want to make string blink (True if yes else False)
- [ ] **hide** is also a boolean type   

> Example 

```ruby
scan(">>>", "orion", "red", False, True)
```

- [ ] **database color** = ["red", "blue", "green", "magenta", "white", "black", "yellow", "orange", "cyan"]

# Print Values

## Using the function print
```python
1. print * "Hello World !"
2. print * "Hello "+"World!", "my name is Karole", "I am 26 years old"
```
- [ ] __*__ separates **print** function with the walues
- [ ] we can print multiple values a same time just list values after **star** separated by comma.
- [ ] **print** function is the default function to output the data with the simplest way.

## Using prompt function from module prompt 
```ruby
from module prompt load prompt 

1. prompt("Hello World !")
2. prompt("Hello "+"World !", [1, 2], True, None)
```
- [ ] this **prompt** function is more powerful than **print** function it was performed to output the data with 
a beautiful style.
- [ ] As in **print** function we can also print multiple data by separating them using comma  
  
# Control flow
## The **if, elif and else** statement

```ruby
if   (conditions):
    <statements>
elif (conditions):
    <statements>
else:
    <statements>
end:
```

> Example1 (if and else) 

```ruby:
if ? 1 == ? integer():
    print * ? integer()
else:
    print * None 
end:
```
> Example2 (if and elif)

```ruby
if 1 % 2 == 0:
    print * True
elif 3 % 2 == 1:
    print * True 
elif 1 not in [1:3]:
    print * False
end:
```

> Example3 (if, elif and else)

```ruby
List = [].random(5)
if 1 in List:
    print * "is found"
elif 2 not in List:
    print * "not found"
else:
    print * None
end:
```

## The **unless and else** statement

```ruby
unless  (conditions):
    <statements>
else:
    <statements>
end:
```

>Example (unless and else)

```ruby:
unless 1==2:
    print * False
else:
    print * True
end:
```

## The **switch** statement
```ruby
swicth (expression):
case value1:
    <statements>
case value2:
    <statements>
default:
    <statements>
end:
```

> Example1 (switch and case)

```ruby
List = rand("int", (0, 10))
switch List:
case 1:
    print * "is 1"
case (1, 2, 5, 9):
    print * "is contained in (1, 2, 5, 9)"
end:
```

> Example2 (switch, case and default)

```ruby
List = rand('norm', (0, 10))
switch List:
case 1:
   print * "is 1"
case 5:
   print * "is 5"
default:
   print * "maybe 2"
end:
```

## The **try** statement
```ruby
try:
   <statements>
except (excpetions)
   <statements>
finally:
   <statements>
end:
``` 
> Example1 (try and except)

```ruby:
try:
   name = 1/0
except:
   print * "error"
end:

try:
   name = 1/0
except zeroDivisionerror:
   print * "division by zero"
end:

try:
   name = m + n
except (NameError, ValueError)
   print * "error"
end:

try:
   name = n + m
except NameError:
   print * "NameError"
except ValueError:
   print * "ValueError"
except Typeerror:
   print * "TypeError"
end:
```

> Example2 (try, except and finally)

```ruby
try:
   name = 1%0
except ZeroDivisionError:
   print * "modulo by zero"
finally:
   name = None
end:
```

# Loops 

## The **for**  loop 

```ruby
for (expression):
    <statements>
end:
```
> Example1 (for)

```ruby
line = 0

for i in range(0, 10):
    line += 1
end:
```

> Example2 (for)

```ruby
str = ""
chars = "1.2.3.4.5.6.7.8.9".split(".")
line = 0

for s in enumerate(chars):
   str += s[1]
   line += s[0]
end:
```
> Example3 (for and only)

```ruby
for i in ([1:10]) only (i % 2 == 0):
    line += i
end:
```

## The **while** loop
```ruby
while (conditions):
    <statements>
end:
```

> Examples1 (while)

```ruby
line, max_n, n = 0, 100, 0

while n < max_n:
   n += 1
end:
```

> Exapmple2 (while)
```ruby
line = 10

while (line > 0 ) and (line % 2 == 1) :
    line -= 1
end:
```

> Example3 (while)
```ruby
line, key = 0.0, False

while key == True:
    line += 1

    if line > 10:
        key = True 
    else:
        pass 
    end
end:
```

# Multiline comments
## The **begin** statement

```ruby
begin:
    <statements>
save as name:
end:
```

> Example1 (just begin)

```ruby
begin:
    my name is Black Mamba, I am a powerful programing language,
    i was created in 2022 by amiehe-essomba, PhD student 
    at universty of Strasbourg, France.
    I was created for solving several problems specially in AI.
    But i need you help to be more powerful.
end:
```

> Example2 (begin and save)

```ruby:
begin:
    my name is Black Mamba...................
save as comment:
end:
```

