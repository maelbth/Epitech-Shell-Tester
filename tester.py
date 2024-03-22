#!/usr/bin/python3

from modules import compare
from shutil import which
from sys import stderr
from json import load
import subprocess
import os

TESTS_PATH = (os.getcwd() + "/tests/tester/tests.json")
BIN_PATH = (os.getcwd() + "/mysh")
REF_PATH = which('tcsh')

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def run(test):
    name = 'name' in test and test['name'] or 'Unamed'
    command = ("\n".join(test['command']) + "\n")

    print(f"- Execute test: {name}.")
    if 'env' in test:
        print("\t→ This test modifies the environments variables.")
        env = test['env']
    else:
        env = None
    ref = subprocess.run(REF_PATH,
        input=command, capture_output=True, text=True, env=env)
    my = subprocess.run(BIN_PATH,
        input=command, capture_output=True, text=True, env=env)

    if 'mismatching' in test:
        passed = compare.mismatch(ref, my, test['mismatching'])
    elif 'matching' in test:
        passed = compare.match(ref, my, test['matching'])
    else:
        passed = compare.result(ref, my)
    if (passed):
        print("✅\tOK: Test passed.\n")
    return (passed)
    

def retrieve_tests():
    with open(TESTS_PATH, "r") as file:
        tests = load(file)
        return (tests)

def main():
    try:
        tests = retrieve_tests()
        passed = 0
        total = 0

        for path in [BIN_PATH, REF_PATH]:
            if (not os.path.isfile(path)):
                print(f"⚠️\tWarning: Unable to locate binary '{path}'.")
                exit(EXIT_FAILURE)
            if (not os.access(path, os.X_OK)):
                print(f"⚠️\tWarning: Permission denied for binary '{path}'.")
                exit(EXIT_FAILURE)

        for test in tests:
            passed = passed + run(test)
            total = total + 1

        if (passed != total):
            print(f"⚠️\tWarning: Some tests failed → {passed}/{total}.")
            exit(EXIT_FAILURE)
        else:
            print("🎉\tSuccess: All tests passed.")
            exit(EXIT_SUCCESS)
    except KeyboardInterrupt:
        print("\n⚠️\tWarning: The tester was canceled !")
    except Exception as error:
        print("⚠️\tWarning:", error, "!", file=stderr)

if (__name__ == "__main__"):
    main()
