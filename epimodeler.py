import numpy as np

class EpiModeler:
    def __init__(self, beta, gamma, S0, I0, R0, days):
        self.beta = beta
        self.gamma = gamma
        self.S = S0
        self.I = I0
        self.R = R0
        self.days = days
        self.results = []

    def run(self):
        for day in range(self.days):
            new_infections = self.beta * self.S * self.I
            new_recoveries = self.gamma * self.I

            self.S -= new_infections
            self.I += new_infections - new_recoveries
            self.R += new_recoveries

            self.results.append((self.S, self.I, self.R))

        return self.results

# Example usage
if __name__ == "__main__":
    model = EpiModeler(beta=0.3, gamma=0.1, S0=0.99, I0=0.01, R0=0, days=160)
    results = model.run()
    print(results)

