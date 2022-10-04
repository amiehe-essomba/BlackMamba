# Classes

To create a class, it must have a name and the choice of the name of a class is not random, it must respect a certain number of criteria: it must start with an upper or lower case letter, it cannot contain only alphabetic characters and the underscore character, its length does not matter. The creation of a __class__ is done using the keyword **class** followed by the name of the class and ends with a **:** to indicate the end of the chain, its closure is done using the keyword **end** followed by **:** 
**A class can only contain classes and functions and nothing else**

## Creating a simple class

- **With initialize() function**
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

## Inheritance class

## Handling files
### Open a file 
```ruby
open(name, file, action, encoding, status)
```
