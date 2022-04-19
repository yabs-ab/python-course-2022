from functools import partial
import threading
import time


def work(n):
    while n > 0:
        n -= 1


def main():
    count = 100_000_000
    t1 = threading.Thread(target=partial(work, count // 2))
    t2 = threading.Thread(target=partial(work, count // 2))

    start_time = time.time()

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time} s")


if __name__ == "__main__":
    main()
