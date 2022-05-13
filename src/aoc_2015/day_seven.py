from pathlib import Path


def parse_instruction(instruction):

    print(f"Parsing\t{instruction}")
    op, bus = instruction.split(" -> ")
    op_parts = op.split(" ")
    if len(op_parts) == 1:
        return Bus(bus, int(op_parts[0]))
    elif len(op_parts) == 2:
        return Gate(op_parts[0], bus, [op_parts[1]])
    else:
        inputs = [op_parts[0]]
        operator_ = op_parts[1]
        if operator_.endswith("SHIFT"):
            operator_ += f"-{op_parts[2]}"
        else:
            inputs.append(op_parts[2])
        return Gate(operator_, bus, inputs)


class Bus:
    def __init__(self, name, value=None, bus_input=None):
        self.name = name
        self.value = value
        self.bus_input = bus_input

    def activate(self):
        if self.bus_input is None and self.value is None:
            raise AttributeError(f"Unexpected Error: {self} has no Value nor Gate as input")
        self.value = self.bus_input.activate()

    def __str__(self) -> str:
        return f"BUS {self.name}, input {self.value}"


class Gate:
    def __init__(self, operator, output, inputs):
        self.operator = operator
        self.output = output
        self.inputs = inputs
        self.input_busses = None

    def activate(self):
        for bus in self.input_busses:
            if bus.value is None:
                bus.activate()
        if self.operator == "AND":
            return self.input_busses[0].value & self.input_busses[1].value
        if self.operator == "OR":
            return self.input_busses[0].value | self.input_busses[1].value
        if self.operator == "NOT":
            return ~self.input_busses[0].value
        if self.operator.startswith("LSHIFT"):
            return ~self.input_busses[0].value << int(self.operator.split("-")[1])
        if self.operator.startswith("RSHIFT"):
            return ~self.input_busses[0].value >> int(self.operator.split("-")[1])


class Circuit:
    def __init__(self, circuit_intructions) -> None:
        self.circuit_intructions = circuit_intructions
        self.buses = {}
        self.gates = []
        self.state = {}

    def add_component(self, component):
        if isinstance(component, Bus):
            # if it is a bus just add to the busses dict
            self.buses[component.name] = component
        else:
            # if it is a gate, add to the gate  list
            self.gates.append(component)
            # also add new busses
            if component.output not in self.buses.keys():
                try:
                    self.buses[component.output] = Bus(component.output, bus_input=component)
                except Exception as e:
                    print(e)

            for input_ in component.inputs:
                if input_ not in self.buses.keys():
                    self.buses[input_] = Bus(input_)

    def run(self):
        for instruction in self.circuit_intructions:
            self.add_component(parse_instruction(instruction))

        # update the gates with the input buses
        for gate in self.gates:
            gate.input_busses = [self.buses[bus] for bus in gate.inputs]

        for bus in self.buses.values():
            if bus.value is None:
                bus.activate()
            self.state[bus.name] = bus.value


if __name__ == "__main__":
    puzzle_input = Path("./src/aoc_2015/input/day_seven.txt")
    circuit_instructions = puzzle_input.open().readlines()
    circuit = Circuit(circuit_instructions)
    # Act
    circuit.run()
