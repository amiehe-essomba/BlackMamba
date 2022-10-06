# Classes

To create a class, it must have a name and the choice of the name of a class is not random, it must respect a certain number of criteria: it must start with an upper or lower case letter, it cannot contain only alphabetic characters and the underscore character, its length does not matter. The creation of a __class__ is done using the keyword **class** followed by the name of the class and ends with a **:** to indicate the end of the chain, its closure is done using the keyword **end** followed by **:** 
**A class can only contain classes and functions and nothing else**

## Creating a simple class
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

<p> You can initialized values in initialize function to make them acceessible directly if functions created inside class </p>

- **Without initialize() function**
```ruby
class math:
    def sum( a : int, b : int = 5) -> integer:
        return a+b
    end:
end:

print * math.sum( a=4, b=-1)

class math:
    class arithmetic:
        def sum( a :int, b : float) -> float:
            return a+b
        end:
    end:
end:

print * math().arithmetic.sum( 4, 3)
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



## Handling files
### Open a file 
```ruby
open(name, file, action, encoding, status)
```
