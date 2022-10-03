<h1 align="center"> Black Mamba </h1>
<p align="ceneter">Black Mamba is an open source object-oriented programming language oriented towards solving machine learning and Deep-learning problems and for the furtur it will be also used for creating web pages. But at the moment it only iused for AI, some packages are written to make it powerful and very useful. Black Mamba represents the futur of interpreted oriented-programming language.</p>

## Built With 
- __**Python**__ 
- __**Cython**__ 
- __**C**__
- __**C++**__

## Language Tools

```ruby
1.  begin/save/as/end
2.  if/elif/else/end
3.  switch/case/default/end
4.  try/except/finally/end
5.  unless/else/end
6.  for/end
7.  while/end
8.  until/end
9.  def/func/end
10. class/end
11. with/end
12. from/module/load/as
13. open/close
14. with/end
```

### Creating a simple class

```ruby
class iris:
    def initialize() -> None:
        self.length = 1.5       # length in centimeter
        self.color  = 'green'   # sheets color
        self.width  = 0.3       # width in centimeter
    end:
    # getting informations 
    def get(type : string = 'color') -> any:
        if type in ['color']:
            return color
        elif type in ['length']:
            return length
        elif type in ['width']:
            return width
        else:
            return 'Error type'
        end:
    end:
end:
```
> more details [here](https://github.com/amiehe-essomba/BlackMamba/blob/BlackMamba/CONTRIBUTING.md).

### Creating a simple function

```ruby
floor = func( master : float ) -> integer :
    str = string( master )      # converting float to a string
    str = str.split('.')        # spliting string
    int = integer(str[0])       # converting string to an integer

    # return the integer part of master
    return int
end:
```
> more details [here](https://github.com/amiehe-essomba/BlackMamba/blob/BlackMamba/Tools.md).

### Open file.
```ruby
open(name='my_file', file='README.md', action='read', encoding='utf-8', status='old')
```
### Read an open file.
```ruby 
my_file.readlines()
```
### Write to an open file 
```ruby
my_file.write('Hello World !\n')
```
### Close an open file
```python
my_file.close()
```

> more details [here](https://github.com/amiehe-essomba/BlackMamba/blob/BlackMamba/Tools.md).

## Select Your IDE 

```python
mamba --T orion
mamba --T pegasus
```

## Project Description 

## Roadmap

## Contributing
pull requests are welcome. Fore major changes, please open an issue first to discuss what you would like to change.
That's very impotant.

Please make sure to update tests as appropriate.
>For more details read the [contribution guidelines](https://github.com/amiehe-essomba/BlackMamba/blob/BlackMamba/Tools.md).

## 🤵 Author 
**Amiehe Essomba** 

- [Profile](https://github.com/amiehe-essomba "Amiehe Essomba" )
- [Website](https://pypi.org/user/amiehe/ "pypi")
- [Twitter](https://twitter.com/irene_essomba?t=dyzm9cjFPhktK4NEtiqtmw&s=09 "@Essomba" )

## Acknowledgement

## 🤝 Support 
Give a ⭐ if you like this project!

## License 
Copyrihght © 2022 **Amiehe Essomba**


This project is licensed under [MIT License](https://github.com/amiehe-essomba/BlackMamba/blob/BlackMamba/LICENSE)

