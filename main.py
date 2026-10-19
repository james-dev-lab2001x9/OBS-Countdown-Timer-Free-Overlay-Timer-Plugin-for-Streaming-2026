"""Entry point for engine."""

from utils import run


def main():
    result = run(50)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
