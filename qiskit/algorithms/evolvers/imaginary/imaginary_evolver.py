# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Interface for Quantum Imaginary Time Evolution."""

from abc import ABC, abstractmethod

from ..evolution_problem import EvolutionProblem
from ..evolution_result import EvolutionResult


class ImaginaryEvolver(ABC):
    """Interface for Quantum Imaginary Time Evolution."""

    @abstractmethod
    def evolve(self, evolution_problem: EvolutionProblem) -> EvolutionResult:
        r"""Perform imaginary time evolution :math:`\exp(-\tau H)|\Psi\rangle`.

        Evolves an initial state :math:`|\Psi\rangle` for an imaginary time :math:`\tau`
        under a Hamiltonian  :math:`H`, as provided in the ``evolution_problem``.

        Args:
            evolution_problem: The definition of the evolution problem.

        Returns:
            Evolution result which includes an evolved quantum state.
        """
        raise NotImplementedError()
