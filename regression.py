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
        self.beta0 = 0
        self.beta1 = 0
        self._methode_fermee()
        self.learning_rate: float = learning_rate
        self.iteration: int = iteration
        self.theta0 = 0
        self.theta1 = 0
        self.km_min = 0
        self.km_max = 0
        self.price_min = 0
        self.price_max = 0
        self.normalized_points = []

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
        self.beta0 = (sum_y - self.beta1 * sum_x) / m

    def gradient_descent(self):
        self.theta0 = 0
        self.theta1 = 0
        len_data = len(self.points)

        for _ in range(self.iteration):
            erreur = 0
            erreur_1 = 0
            for i in range(len_data):
                estimate_price = self.theta0 + self.theta1 * self.points[i][0]
                tmp_erreur = estimate_price - self.points[i][1]
                erreur += tmp_erreur
                erreur_1 += tmp_erreur * self.points[i][0]
            erreur /= len_data
            erreur_1 /= len_data
            self.theta0 -= self.learning_rate * erreur
            self.theta1 -= self.learning_rate * erreur_1
        self.print_theta()
        print(f'e:{erreur}-e1:{erreur_1}')

    def _denormalize_thetas(self):
        theta1_real = self.theta1 * \
            (self.price_max - self.price_min) / (self.km_max - self.km_min)
        theta0_real = self.price_min + self.theta0 * (self.price_max - self.price_min) \
            - theta1_real * self.km_min
        return theta0_real, theta1_real

    def gradient_descent_norm(self):
        self.theta0 = 0
        self.theta1 = 0
        len_data = len(self.points)
        self._normalize()

        for _ in range(self.iteration):
            erreur = 0
            erreur_1 = 0
            for i in range(len_data):
                estimate_price = self.theta0 + \
                    self.theta1 * self.normalized_points[i][0]
                tmp_erreur = estimate_price - self.normalized_points[i][1]
                erreur += tmp_erreur
                erreur_1 += tmp_erreur * self.normalized_points[i][0]
            erreur /= len_data
            erreur_1 /= len_data
            self.theta0 -= self.learning_rate * erreur
            self.theta1 -= self.learning_rate * erreur_1

        self.theta0, self.theta1 = self._denormalize_thetas()

    def _normalize(self):
        self.km_min = min(p[0] for p in self.points)
        self.km_max = max(p[0] for p in self.points)
        self.price_min = min(p[1] for p in self.points)
        self.price_max = max(p[1] for p in self.points)

        self.normalized_points = [
            (
                (km - self.km_min) / (self.km_max - self.km_min),
                (price - self.price_min) / (self.price_max - self.price_min)
            )
            for km, price in self.points
        ]

    def print_theta(self):
        print(f'theta0: {self.theta0}\ntheta1: {self.theta1}')

    def print_beta(self):
        print(f'beta0: {self.beta0}\nBeta1: {self.beta1}')

    def print_result(self):
        print(f'beta0: {self.beta0}beta1: {self.beta1}')
        print(f'theta0: {self.theta0}theta1: {self.theta1}')
        print(f'-a {self.theta0} -x {self.theta1}')

    def print_points(self):
        for x, y in self.points:
            print(x, y)

    def plotting_graph(self):
        pass

    def result_graph(self):
        pass
