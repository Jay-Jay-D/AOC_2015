import pytest

from aoc_2015.day_seven import Bus, Circuit, Gate, parse_instruction

circuit_intructions = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i",
]


expected_circuit_output = {
    "d": 72,
    "e": 507,
    "f": 492,
    "g": 114,
    "h": 65412,
    "i": 65079,
    "x": 123,
    "y": 456,
}

gates_cases = [
    pytest.param("x AND y -> d", "AND", "d", ["x", "y"], id="x AND y -> d"),
    pytest.param("x LSHIFT 2 -> f", "LSHIFT", "f", ["x"], id="x LSHIFT 2 -> f"),
    pytest.param("NOT y -> i", "NOT", "i", ["y"], id="NOT y -> i"),
]


def test_parse_instructions_bus():
    # Arrange
    instruction = "123 -> x"
    expected_bus = Bus("x", 123)
    # Act
    actual_bus = parse_instruction(instruction)
    # Assert
    assert isinstance(actual_bus, Bus)
    assert expected_bus.value == actual_bus.value
    assert expected_bus.bus_input is None


def test_parse_instructions_bus():
    # Arrange
    instruction = "a -> y"
    expected_bus = Bus("y", value=None, bus_input="a")
    # Act
    actual_bus = parse_instruction(instruction)
    # Assert
    assert isinstance(actual_bus, Bus)
    assert expected_bus.value == actual_bus.value
    assert expected_bus.bus_input == "a"


@pytest.mark.parametrize(
    "instruction,expected_operator,expected_output,expected_inputs", gates_cases
)
def test_parse_instructions_gate(instruction, expected_operator, expected_output, expected_inputs):
    # Arrange
    expected_gate = Gate(expected_operator, expected_output, expected_inputs)
    # Act
    actual_gate = parse_instruction(instruction)
    # Assert
    assert isinstance(actual_gate, Gate)
    assert expected_gate.operator == expected_operator
    assert expected_gate.output == expected_output
    assert expected_gate.inputs == expected_inputs


def test_add_gate():
    # Arrange
    circuit = Circuit(["123 -> x", "456 -> y"])
    circuit.run()
    # Check state is as expected
    for bus, value in {"x": 123, "y": 456}.items():
        assert bus in circuit.buses.keys()
        assert circuit.buses[bus].value == value
        assert circuit.buses[bus].bus_input is None

    new_components = {"d": "x AND y -> d", "i": "NOT y -> i", "g": "d OR i -> g"}

    # Act and Assert
    for new_bus, instruction in new_components.items():
        component = parse_instruction(instruction)
        circuit.add_component(component)
        assert component in circuit.gates
        assert new_bus in circuit.buses.keys()
        assert circuit.buses[new_bus].value is None
        assert isinstance(circuit.buses[new_bus].bus_input, Gate)


def test_operators():
    # Arrange
    circuit_instructions = ["123 -> x", "456 -> y", "x AND y -> d"]
    circuit = Circuit(circuit_instructions)
    # Act
    circuit.run()
    # Assert
    assert circuit.buses["d"].value == 72


def test_circuit():
    # Arrange
    circuit = Circuit(circuit_intructions)
    # Act
    circuit.run()
    # Assert
    assert circuit.state == expected_circuit_output
