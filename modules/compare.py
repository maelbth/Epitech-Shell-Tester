
def result(ref, my):
    if (ref.stdout != my.stdout):
        reason = "Standard output doesn't match.\n"
        details = f"\nExpected :\n{ref.stdout}\n\nGot :\n{my.stdout}\n"
        return (False, reason + details)
    if (ref.stderr != my.stderr):
        reason = "Error output doesn't match.\n"
        details = f"\nExpected :\n{ref.stderr}\n\nGot :\n{my.stderr}\n"
        return (False, reason + details)
    if (ref.returncode != my.returncode):
        reason = "Exit status doesn't match.\n"
        details = f"\nExpected :\n{ref.returncode}\n\nGot :\n{my.returncode}\n"
        return (False, reason + details)
    return (True, None)

def mismatch(my, ref, patterns):
    for pattern in patterns:
        if pattern in my.stdout:
            reason = f"Found '{pattern}' in mysh.\n"
            return (False, reason)
    if (ref.returncode != my.returncode):
        reason = "Exit status doesn't match.\n"
        details = f"\nExpected :\n{ref.returncode}\n\nGot :\n{my.returncode}\n"
        return (False, reason + details)
    return (True, None)

def match(ref, my, patterns):
    for pattern in patterns:
        if not pattern in my.stdout:
            reason = f"Found '{pattern}' in mysh.\n"
            return (False, reason)
    if (ref.returncode != my.returncode):
        reason = "Exit status doesn't match.\n"
        details = f"\nExpected :\n{ref.returncode}\n\nGot :\n{my.returncode}\n"
        return (False, reason + details)
    return (True, None)
