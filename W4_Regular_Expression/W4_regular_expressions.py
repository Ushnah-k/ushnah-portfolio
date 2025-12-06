# W4_regular_expressions.py
#ushnahk
#During the preparation of this assignment, ushnah khan used ChatGPT
#in setting up the four methods to accurately explain to me what each thing does. I also
#used AI to get an indepth explaination of everything new im learning.
#After using this tool, I/we reviewed and edited the content as needed to ensure its
#accuracy and take full responsibility for the content in relation to grading.

import re   # Python's built-in "regular expressions" module.
            # Regex lets us match, search, replace, and validate text patterns.

# 🔹 NOTE ABOUT r"...":
# In regex, we often use backslashes like \d (digit), \s (space), \b (word boundary).
# In normal Python strings, backslashes are escape characters (e.g. "\n" = newline).
# If we wrote regex without raw strings, we'd need to DOUBLE the backslashes, like "\\d".
# Using r"...", called a RAW STRING, tells Python:
#    "Don’t treat backslashes as escape codes, take them literally."
# Example:
#    print("\n")   -> makes a newline
#    print(r"\n")  -> prints the characters \ and n
#
# That’s why you see r"..." in patterns like r"[A-Za-z0-9]+"
# (good habit, even though this specific one doesn’t use backslashes).
#
# In find_literals we don’t use r"..." because we’re not writing a raw regex ourselves —
# we generate it with re.escape(substring), which already handles escapes safely.


def contains_only_alphanumeric(string):
    """
    Return True if string contains ONLY a-z, A-Z, 0-9 (at least one char), else False.
    Uses re.fullmatch.
    """
    # Pattern: [A-Za-z0-9]+
    #   A-Z  → uppercase letters
    #   a-z  → lowercase letters
    #   0-9  → digits
    #   +    → one or more characters
    #
    # re.fullmatch checks if the ENTIRE string matches this pattern
    # We use r"..." (raw string) because regex often needs backslashes, and raw
    # strings prevent Python from confusing them with escape sequences.
    return re.fullmatch(r"[A-Za-z0-9]+", string) is not None


def find_literals(substring, string):
    """
    Return True if 'substring' appears literally anywhere inside 'string', else False.
    Uses re.search with re.escape so special chars are treated literally.
    """
    # re.escape(substring) makes sure special characters like "+" or "?" are
    # treated as normal text instead of regex operators.
    # Because re.escape already produces a safe regex, we don’t need to add r"..."
    pattern = re.escape(substring)

    # re.search checks if the pattern appears ANYWHERE in the string
    return re.search(pattern, string) is not None


def remove_parentheses(string):
    """
    Remove any ' ( ... )' blocks and any leading spaces directly before them.
    Uses re.sub.
    """
    # Pattern: \s*\([^)]*\)
    #   \s*     → zero or more spaces
    #   \(      → literal "("
    #   [^)]*   → zero or more characters that are NOT ")"
    #   \)      → literal ")"
    #
    # Here we MUST use r"..." because of all the backslashes — otherwise
    # Python would think \( means a literal "(" escape code (which doesn’t exist).
    cleaned = re.sub(r"\s*\([^)]*\)", "", string)

    # .strip() removes spaces left at the ends of the string
    return cleaned.strip()


def match_words(string):
    """
    Return True if TWO words in the string start with uppercase 'P', else False.
    Uses re.findall.
    """
    # Pattern: \bP\w*
    #   \b     → word boundary (start of a word)
    #   P      → literal capital P
    #   \w*    → zero or more "word" characters (letters, digits, underscore)
    #
    # Again, we use r"..." to avoid issues with \b and \w.
    starts_with_P = re.findall(r"\bP\w*", string)

    # If there are 2 or more such words, return True
    return len(starts_with_P) >= 2


# ----------------- quick demo/tests (optional) -----------------
if __name__ == "__main__":
    # contains_only_alphanumeric
    print(contains_only_alphanumeric("ABCDEFabcdef123450"))  # True
    print(contains_only_alphanumeric("hello"))               # True
    print(contains_only_alphanumeric("*&%@#!}{"))            # False
    print(contains_only_alphanumeric("hello!"))              # False

    # find_literals
    sample = "The quick brown fox jumps over the lazy dog."
    print(find_literals("fox", sample))    # True
    print(find_literals("dog", sample))    # True
    print(find_literals("horse", sample))  # False

    # remove_parentheses
    for s in ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]:
        print(remove_parentheses(s))
        # expected:
        # example
        # w3resource
        # github
        # stackoverflow

    # match_words
    print(match_words("Python PHP"))       # True
    print(match_words("Java JavaScript"))  # False
    print(match_words("C C++"))            # False
