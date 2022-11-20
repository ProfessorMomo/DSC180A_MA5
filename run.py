import sys
import os
import json

sys.path.insert(0, 'src')

import env_setup
from etl import get_data, read_test
from features import apply_features

from model import model_build


def main(targets):
    '''
    Runs the 'test' target on the test data to ensure the pipeline works without errors
    '''

    env_setup.make_datadir()
    env_setup.auth()

    if 'test' in targets:
        train_data = get_data("data")
        test_data = read_test("data")
        
        

    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv
    main(targets)
