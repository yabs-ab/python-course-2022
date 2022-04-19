from functools import partial
import multiprocessing as mp
import time


def work(n):
    while n > 0:
        n -= 1


def main():
    count = 100_000_000
    p1 = mp.Process(target=partial(work, count // 2))
    p2 = mp.Process(target=partial(work, count // 2))

    start_time = time.time()

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time} s")


if __name__ == "__main__":
    main()
