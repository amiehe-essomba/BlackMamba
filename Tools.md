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

# 
print * iris().get()
```

- **Without initialize() function**
```ruby
class math:
    def sum( a : int, b : int = 5) -> integer:
        return a+b
    end:
end:

class math:
    class arithmetic:
        def sum( a :int, b : float) -> float:
            return a+b
        end:
    end:
end:
```

## Inheritance class

## Handling files
### Open a file 
```ruby
open(name, file, action, encoding, status)
```
