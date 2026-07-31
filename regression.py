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
        self.beta0 = 0
        self.beta1 = 0
        self._methode_fermee()
        self._gradient_descent()

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

    def _methode_fermee(self):
        x = self.points[:, 0]
        y = self.points[:, 1]
        m = len(x)
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xy = np.sum(x * y)
        sum_x2 = np.sum(x * x)
        self.beta1 = (m * sum_xy - sum_x * sum_y) / \
            (m * sum_x2 - sum_x * sum_x)
        self.beta2 = (sum_y - self.theta1 * sum_x) / m

    def _gradient_descent(self):
        x = self.points[:, 0]  # mileage
        y = self.points[:, 1]  # price
        m = len(x)

        for _ in range(self.iteration):
            predictions = self.theta0 + self.theta1 * x
            errors = predictions - y

            tmp_theta0 = self.learning_rate * (1/m) * np.sum(errors)
            tmp_theta1 = self.learning_rate * (1/m) * np.sum(errors * x)
            self.theta0 -= tmp_theta0
            self.theta1 -= tmp_theta1

    def print_result(self):
        print(f'beta0: {self.beta0}\ntbeta1: {self.beta1}\n')
        print(f'theta0: {self.theta0}\ntheta1: {self.theta1}\n')
        print(f'-a {self.theta0} -x {self.theta1}\n')

    def print_points(self):
        for x, y in self.points:
            print(x, y)

    def plotting_graph(self):
        pass

    def result_graph(self):
        pass
