# Classes

To create a class, it must have a name and the choice of the name of a class is not random, it must respect a certain number of criteria: it must start with an upper or lower case letter, it cannot contain only alphabetic characters and the underscore character, its length does not matter. The creation of a __class__ is done using the keyword **class** followed by the name of the class and ends with a **:** to indicate the end of the chain, its closure is done using the keyword **end** followed by **:** 
**A class can only contain classes and functions and nothing else**

## Creating a class
- **Using __initialize()__ function to make variables global**

```ruby
class iris:
    def initialize() -> None
        self.color  = 'green'
        self.length = 1.5
        self.width  = 0.3
    end:
end:
```

- **Defining default values inside __initialize()__**

```ruby
class iris:
    def initialize( color : string = 'green') -> None:
        self.color  = color
        self.length = 1.5
        self.width  = 0.3
    end:
end:
```

The **initialize()** function returning no value its output is always set to **None**.
It is also possible to define some variables in this function to make them more accessible in all functions connected to the host class, so no need to create several variables for each function. These variables created in the **initialize()** function are called **semi-global** because in general to create a pure global variable it is necessary to use the **global** function (see later), these variables are not only accessible in all classes, and functions they can be used throughout the code it's up to you to decide which statement works best for you.
In the **initialize()** function you can also define default values as illustrated above.
The use of this function is really very practical and very useful, however if it is created it must be the first to appear in a class because it is an initialization function and cannot be called in the code or even the entire program.


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


## Inheritance classes`

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

It is possible to have access to the different information of another class, namely: its different functions and thus use them in the host class, it is also possible to obtain the semi-global variables created in the **initialize()** function if it was created in this class. This could be extremely efficient, it is also possible to associate the functions of this class to the host class as shown in the example above.
We start by creating a class setosa containing only the semi-global variables of this class just to simplify things then a second class is created ( host class ), the class iris will host the class setosa just by defining setosa between brackets and so iris can access all of setosa's information down to the smallest detail.

## Multiple inheritances


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

It is also possible for a class to inherit the properties of several classes at the same time as the example above demonstrates.

## Multidimensional classes

```ruby
class math:
    def initilaize( a : int = 0) -> None:
        self.a = a
    end:
    
    # creating a sub-class
    class arithmetic:
        def initalize( b : int ) -> None:
            self.b = b
        end:
        
        #creatng sub-function
        def mean( c : float) -> float:
            return (a+b+c)/3.0
        end:
    end:
end:

print * math(a = 4).arithmetic(b = -4 ).sum(c = 2.0)
```
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

The default value is **any** it means that the output can be any type.
The type of a function is defined as follows:

```ruby
prod = func() -> list:
prod = func() -> tuple:
prod = func() -> any:
```

## Variables Type in a function.

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

### Variables Type in function

## Creating a function using **func** as a keyword
```ruby
sum = func() -> list:
    return [].random((10, (100, 300)))
end:
```

