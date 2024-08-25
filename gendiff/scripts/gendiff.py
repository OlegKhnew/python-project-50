#!/usr/bin/env python3

"""Main launch file."""

from gendiff.engine import generate_diff
from gendiff.cli import cli


def main():
    """General launch function."""
    first_file, second_file, format = cli()
    result = generate_diff(first_file, second_file, format)
    print(result)


if __name__ == '__main__':
    main()
