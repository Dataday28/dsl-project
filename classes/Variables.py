class Variables:

    def var_declaration(self, variables, name, value = None):
        variables[str(name)] = value
        print(f"Variable {name} establecida con el valor {value}")
        return None  # Assignment does not return a value

    def var_assigment(self, variables, name, value):
        if name in variables:
            variables[name] = value
            print(f"Variable {name} updated with value {value}")
        else:
            print(f"\n Error: Variable {name} no declarada \n")