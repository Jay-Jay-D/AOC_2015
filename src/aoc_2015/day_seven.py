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
        if self.bus_input is None and self.value is None:
            raise AttributeError(f"Unexpected Error: {self} has no Value nor Gate as input")
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
        self.fixed_buses = {}

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

    def wire_gates(self):
        for gate in self.gates:
            for bus in gate.inputs:
                if bus in self.buses.keys():
                    gate.input_busses.append(self.buses[bus])
                # When one of the gates input is a number (known case 1)
                else:
                    gate.input_busses.append(Bus(str(uuid4()), value=int(bus)))

    def refresh(self):
        for bus in self.buses.values():
            bus.value = None
        self.state = {}
        for bus, value in self.fixed_buses.items():
            self.buses[bus].value = value

    def run(self):
        for instruction in self.circuit_intructions:
            component = parse_instruction(instruction)
            # Part 2 - after refreshing we need to keep the instructions for fixed buses
            # e.g. 123 -> x
            if isinstance(component, Bus) and component.value is not None:
                self.fixed_buses[component.name] = component.value
            self.add_component(component)

        # update the gates with the input buses
        self.wire_gates()

        for bus in self.buses.values():
            if isinstance(bus.bus_input, str) and bus.bus_input in self.buses.keys():
                bus.bus_input = self.buses[bus.bus_input]
            self.state[bus.name] = bus.activate()


if __name__ == "__main__":
    puzzle_input = Path("./src/aoc_2015/input/day_seven.txt")
    circuit_instructions = puzzle_input.open().readlines()
    circuit = Circuit(circuit_instructions)

    circuit.run()
    print(f'Part 1 - bus a value: {circuit.state["a"]}')
    a_bus_value = circuit.state["a"]
    circuit.refresh()
    circuit.buses["b"].value = a_bus_value
    circuit.run()
    print(f'Part 2 - bus a value: {circuit.state["a"]}')
