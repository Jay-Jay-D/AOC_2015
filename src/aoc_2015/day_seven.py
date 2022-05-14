from curses.ascii import isdigit
from pathlib import Path

from uuid import uuid4


def parse_instruction(instruction):
    op, bus = instruction.strip().split(" -> ")
    op_parts = op.split(" ")

    # Buses
    if len(op_parts) == 1:
        if all(isdigit(c) for c in op_parts[0]):
            # Case 123 -> b
            return Bus(bus, int(op_parts[0]))
        else:
            # Case a -> b
            return Bus(bus, bus_input=op_parts[0])

    # Gate NOT
    if len(op_parts) == 2:
        return Gate(op_parts[0], bus, [op_parts[1]])

    inputs = [op_parts[0]]
    operator_ = op_parts[1]
    if operator_.endswith("SHIFT"):
        # Shift gates
        operator_ += f"-{op_parts[2]}"
    else:
        # AND and OR gates
        inputs.append(op_parts[2])
    return Gate(operator_, bus, inputs)


class Bus:
    def __init__(self, name, value=None, bus_input=None):
        self.name = name
        self.value = value
        self.bus_input = bus_input

    def activate(self):
        if self.value is None:
            self.value = self.bus_input.activate()
        return self.value

    def __str__(self) -> str:
        return f"BUS {self.name}, input {self.value}"


class Gate:
    def __init__(self, operator, output, inputs):
        self.operator = operator
        self.output = output
        self.inputs = inputs
        self.input_busses = []

    def activate(self):
        for bus in self.input_busses:
            if bus.value is None:
                bus.activate()
        if self.operator == "AND":
            return self.input_busses[0].value & self.input_busses[1].value
        if self.operator == "OR":
            return self.input_busses[0].value | self.input_busses[1].value
        if self.operator == "NOT":
            return ~self.input_busses[0].value & 0xFFFF
        if self.operator.startswith("LSHIFT"):
            return self.input_busses[0].value << int(self.operator.split("-")[1])
        if self.operator.startswith("RSHIFT"):
            return self.input_busses[0].value >> int(self.operator.split("-")[1])


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

    def run(self):
        for instruction in self.circuit_intructions:
            self.add_component(parse_instruction(instruction))

        # update the gates with the input buses
        for gate in self.gates:
            for bus in gate.inputs:
                if bus in self.buses.keys():
                    gate.input_busses.append(self.buses[bus])
                # When one of the gates input is 1
                else:
                    gate.input_busses.append(Bus(str(uuid4()), value=int(bus)))

        for bus in self.buses.values():
            if isinstance(bus.bus_input, str) and bus.bus_input in self.buses.keys():
                bus.bus_input = self.buses[bus.bus_input]
            self.state[bus.name] = bus.activate()


if __name__ == "__main__":
    puzzle_input = Path("./src/aoc_2015/input/day_seven.txt")
    circuit_instructions = puzzle_input.open().readlines()
    circuit = Circuit(circuit_instructions)
    # Act
    circuit.run()
    print(circuit.state["a"])
