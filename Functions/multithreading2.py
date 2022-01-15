import multiprocessing
import os
import threading


def main():
    print("Number of cores: ", multiprocessing.cpu_count())


if __name__ == "__main__":
    main()
