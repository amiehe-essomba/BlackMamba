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
    def get( item : string ):
        if item == 'color':
            return color
        elif item == 'width':
            return width
        elif item == 'size':
            return size
        else:
            return 'item Error'
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
