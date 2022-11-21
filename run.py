import sys
import os
import json
import numpy as np

sys.path.insert(0, 'src')

from etl import get_data, read_test

from model import build_and_predict


def main(targets):
    '''
    Runs the 'test' target on the test data to ensure the pipeline works without errors
    '''

    if 'test' in targets:
        train_data = get_data("data")
        test_data = read_test("data")
        build_and_predict(train_data, test_data)

    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv
    main(targets)

    print("Predictions were made and saved to test folder")
