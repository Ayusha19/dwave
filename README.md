# Grover's search algorithm

There are problems for which it's easy to check if a proposed solution is correct.
We can convert an algorithm that checks solutions into a quantum circuit that changes the phase of solution states
We can then use Grover's algorithm to work out which states have their phases changed.

## Overview of Grover's algorithm

1) The first step is to create an equal superposition of every possible input to the oracle. If our qubits all start in the state |0> , we can create this superposition by applying a H-gate to each qubit. We’ll call this equal superposition state '|s>'.

