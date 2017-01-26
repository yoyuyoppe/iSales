import argparse


def create_parser_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', '--user')
    parser.add_argument('-P', '--passw')

    return parser
