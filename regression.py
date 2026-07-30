import csv
import sys
import numpy as np


class Regression:
    def __init__(self, path: str,
                 learning_rate: float = 0.01,
                 iteration: int = 1000
                 ):
        self.datapath: str = path
        self._check_file()
        self.points = []
        self._get_points()
        self.learning_rate: float = learning_rate
        self.iteration: int = iteration
        self.theta0 = 0
        self.theta1 = 0

    def _check_file(self):
        try:
            with open(self.datapath, 'r') as f:
                reader = csv.reader(f)
                header = next(reader)
                if len(header) != 2:
                    raise ValueError("Plus de deux colonnes")
                for line_num, row in enumerate(reader, start=2):

                    if len(row) != 2:
                        raise ValueError(
                            f"Ligne {line_num}: plus de 2 valeurs"
                        )
                    for col_num, value in enumerate(row, start=1):
                        try:
                            float(value)
                        except ValueError:
                            raise ValueError(f"L {line_num} C {
                                             col_num}: '{value}'")
            return True
        except ValueError as e:
            print(f"CSV invalide: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)

    def _get_points(self):
        self.points = np.genfromtxt(
            self.datapath, delimiter=',', skip_header=1)

    def _calcul(self):
        pass

    def print_result(self):
        print(f'theta0: {self.theta0}\ntheta1: {self.theta1}\n')
        print(f'-a {self.theta0} -x {self.theta1}\n')

    def print_points(self):
        for x, y in self.points:
            print(x, y)

    def plotting_graph(self):
        pass

    def result_graph(self):
        pass
