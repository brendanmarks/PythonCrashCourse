import pizzaimport #imports whole pizzaimport
import pizzaimport as p # creating an alias for pizzaimport
from pizzaimport import * #import all functions (this no longer requires dot notation)
from pizzaimport import make_pizza as mp # alternative way to just import one function

p.make_pizza(16, 'pepperoni')

mp(12, 'mushrooms', 'green peppers', 'extra cheese')
