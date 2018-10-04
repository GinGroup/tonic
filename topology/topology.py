'''
    This is a class for Topology generation.
'''
import warnings

class Parameter():
    def __init__(self, value, variable = True):
        self.value = value
        self.variable = variable
    
    def __str__(self):
        _parameter_info = {"value": self.value, "variable": self.variable}
        return str(_parameter_info)

    def __add__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            value = self.value + other
            return Parameter(value, self.variable)
        elif (isinstance(other, Parameter)):
            value = self.value + other.value
            variable = self.variable and other.variable
            return Parameter(value, variable)
        else:
            raise ValueError("int, float value or Parameter is required")
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            value = self.value - other
            return Parameter(value, self.variable)
        elif (isinstance(other, Parameter)):
            value = self.value - other.value
            variable = self.variable and other.variable
            return Parameter(value, variable)
        else:
            raise ValueError("int, float value or Parameter is required")

    def __rsub__(self, other):
        raise NotImplementedError

    def __iadd__(self, other):
        if (isinstance(other, int) or isinstance(other, float) or isinstance(other, Parameter)):
            self.value += other.value
            return self
        else:
            raise ValueError("int, float value or Parameter is required")

class Topology():
    def __init__(self):
        self.entities = []
        self.topology_parameters = []
        pass

    def add_entity(self, entity):
        self.entities.append(entity)

class Geometric_entity():
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.parameters = []
        for arg in args:
            if (isinstance(arg, list) or isinstance(arg, tuple)):
                for arg_element in arg:
                    self._add_new_parameter(arg_element)
            else:
                self._add_new_parameter(arg)

        #self._init_parameters(kwargs)

    def __str__(self):
        _entity_info = self.__class__.__name__ + " entity\n" 
        _entity_info += str(len(self.parameters)) +  " Parameters: " 
        _entity_info += str([str(parameter) for parameter in self.parameters])
        return _entity_info

    def _add_new_parameter(self, new_parameter):

        if (new_parameter not in self.parameters):
            self.parameters.append(new_parameter)

    def _init_parameters(self, parameters):
        self.parameters.update((k, parameters[k]) for k in self.parameters.keys() & parameters.keys())

    def update_parameters(self, **parameters):
        for key in parameters.keys():
            if key not in self.parameters.keys():
                message = 'This key (' + str(key) + ') is not in the original parameter set. It will not be updated or used.'
                warnings.warn(message, SyntaxWarning)

        self.parameters.update((k, parameters[k]) for k in self.parameters.keys() & parameters.keys())

class Cylinder(Geometric_entity):
    def __init__(self, **kwargs):
        self.parameters = {'x': None, 'y': None, 'R': None}
        Geometric_entity.__init__(self, **kwargs)

class Line(Geometric_entity):
    def __init__(self, *args, **kwargs):
        Geometric_entity.__init__(self, *args, **kwargs)
        
        if len(args) == 2:
            self.a = args[0]
            self.b = args[1]
        elif len(args) == 4:
            self.a = [args[0], args[1]]
            self.b = [args[2], args[3]]
        else:
            raise SyntaxError("Only 2 or 4 arguments accepted to create a Line.")
    
    

def Point(x, y):
    return [x, y]

if __name__ == "__main__":

    p1 = Parameter(0.)
    p2 = Parameter(0.)
    p3 = Parameter(1.)

    point1 = Point(p1, p2)
    point2 = Point(p3, p3)
    line = Line(point1, point2)
    print(line)
