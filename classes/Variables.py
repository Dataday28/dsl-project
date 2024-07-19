class Variables:

    def var_declaration(self, variables, name, value):
        variables[name] = value
        print(f"Variable {name} establecida con el valor {value}")

    def var_assigment(self, variables, name, value):
        if name in variables:
            variables[name] = value
            print(f"Variable {name} updated with value {value}")
        else:
            print(f"Error: Variable {name} not declared")