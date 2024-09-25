import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Run benchmarks.')
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument('--benchmark_items', type=str, required=True, help='Comma-separated list of benchmark items')

    def parse_arguments(self):
        return self.parser.parse_args()