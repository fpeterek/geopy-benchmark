from typing import List, Callable, Tuple
import time

from point import Point


class Benchmark:

    def __init__(self, ref_size: int, sample_size: int):
        self.ref = Benchmark.gen_points(ref_size)
        self.sample = Benchmark.gen_points(sample_size)

    @staticmethod
    def gen_points(num: int) -> List[Point]:
        return [Point.random() for _ in range(num)]

    def closest(self, point: Point, fn: Callable) -> Point:
        return min(self.ref, key=lambda p: fn(point, p))

    def measure_fn_time(self, fn: Callable):
        begin = time.time_ns()

        for point in self.sample:
            self.closest(point, fn)

        end = time.time_ns()
        return (end-begin) / 10**9

    def measure_times(self) -> Tuple[float, float, float]:
        euc = self.measure_fn_time(Point.euc)
        man = self.measure_fn_time(Point.man)
        geo = self.measure_fn_time(Point.dist)

        return euc, man, geo

    def measure_accuracy(self) -> Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]]:
        euc, man, geo = 0, 0, 0

        euc_dist, man_dist = 0.0, 0.0

        for point in self.sample:
            geo_p = self.closest(point, Point.dist)
            euc_p = self.closest(point, Point.euc)
            man_p = self.closest(point, Point.man)

            geo += 1
            if geo_p == euc_p:
                euc += 1
            else:
                euc_dist += abs(point.dist(geo_p) - point.dist(euc_p))
            if geo_p == man_p:
                man += 1
            else:
                man_dist += abs(point.dist(geo_p) - point.dist(man_p))

        return (euc / geo, euc_dist / (geo-euc)), (man / geo, man_dist / (geo-man)), (1.0, 0.0)

    def run_time_benchmark(self):
        euc, man, geo = self.measure_times()

        print(f'Euclidean distance: {euc} s')
        print(f'Manhattan distance: {man} s')
        print(f'GeoPy distance: {geo} s')

    def run_accuracy_benchmark(self):
        euc, man, geo = self.measure_accuracy()
        euc, euc_err = euc
        man, man_err = man
        geo, _ = geo

        print(f'Euclidean accuracy: {int(euc*100) / 100} (avg error: {int(euc_err)} m)')
        print(f'Manhattan accuracy: {int(man*100) / 100} (avg error: {int(man_err)} m)')
        print(f'GeoPy accuracy: {int(geo*100) / 100}')

    def run_benchmark(self):
        # self.run_time_benchmark()
        self.run_accuracy_benchmark()


def main():
    benchmark = Benchmark(30, 100_000)
    benchmark.run_benchmark()
