
def result(ref, my):
    if (ref.stdout != my.stdout):
        print("❌\tKO: Test failed: Standard output doesn't match.\n")
        print(f"\nExpected :\n{ref.stdout}\n\nGot :\n{my.stdout}\n")
        return (False)
    if (ref.stderr != my.stderr):
        print("❌\tKO: Test failed: Error output doesn't match.\n")
        print(f"\nExpected :\n{ref.stderr}\n\nGot :\n{my.stderr}\n")
        return (False)
    if (ref.returncode != my.returncode):
        print("❌\tKO: Test failed: Exit status doesn't match.\n")
        print(f"\nExpected :\n{ref.returncode}\n\nGot :\n{my.returncode}\n")
        return (False)
    return (True)

def mismatch(my, ref, patterns):
    for pattern in patterns:
        if pattern in my.stdout:
            print(f"❌\tKO: Test failed: Found '{pattern}' in mysh.\n")
            return (False)
    if (ref.returncode != my.returncode):
        print("❌\tKO: Test failed: Exit status doesn't match.\n")
        print(f"\nExpected :\n{ref.returncode}\n\nGot :\n{my.returncode}\n")
        return (False)
    return (True)

def match(ref, my, patterns):
    for pattern in patterns:
        if not pattern in my.stdout:
            print(f"❌\tKO: Test failed: Can't find '{pattern}' in mysh.\n")
            return (False)
    if (ref.returncode != my.returncode):
        print("❌\tKO: Test failed: Exit status doesn't match.\n")
        print(f"\nExpected :\n{ref.returncode}\n\nGot :\n{my.returncode}\n")
        return (False)
    return (True)
