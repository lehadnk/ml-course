class LinearRegressor:
    def __init__(self, train_data):
        num_axes = len(train_data[0])
        y_axis_number = num_axes - 1

        axis_values = [[] for _ in range(num_axes)]
        for x in train_data:
            for i in range(num_axes):
                axis_values[i].append(x[i])

        averages = [sum(axis_values[i]) / len(axis_values[i]) for i in range(num_axes)]
        y_average = averages[y_axis_number]

        deviations = [[] for i in range(num_axes)]
        for i in range(num_axes):
            deviations[i] = [x - averages[i] for x in axis_values[i]]

        X_deviations = deviations[:y_axis_number]
        y_deviations = deviations[y_axis_number]

        numerators = [[] for i in range(num_axes - 1)]
        for i in range(num_axes - 1):
            numerators[i] = [X_deviations[i][j] * y_deviations[j] for j in range(len(X_deviations[i]))]

        numerators = [sum(numerators[i]) for i in range(num_axes - 1)]

        denumerators = [[] for i in range(num_axes - 1)]
        for i in range(num_axes - 1):
            denumerators[i] = [X_deviations[i][j] ** 2 for j in range(len(X_deviations[i]))]

        denumerators = [sum(denumerators[i]) for i in range(num_axes - 1)]

        self.coefficients = [numerators[i] / denumerators[i] if denumerators[i] != 0 else 0 for i in range(num_axes - 1)]
        self.adjustment = y_average - sum([self.coefficients[i] * averages[i] for i in range(num_axes - 1)])

    def predict(self, point):
        return self.adjustment + sum([point[i] * self.coefficients[i] for i in range(len(self.coefficients))])