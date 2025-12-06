'''
Homework Week 4: Wannabe Palindrome Problem (Part A)

Name: Ushnah Khan
Email: ushnahk@vt.edu
Date: 9/19/2025

I have neither given nor received unauthorized 
assistance on this assignment.



During the preparation of this assignment, I used ChatGPT
to plan a center-expansion approach that allows one interior
fault (mismatch or deletion), to debug edge cases 
(avoiding faults at the ends), and to fix indentation issues
in VS Code. I reviewed and edited the code and take full
responsibility for its correctness.

Objective: The goal of this assignment is to develop 
an efficient solution for finding the longest "wannabe
palindromic substring" of a given input string. 
A wannabe palindrome is defined as a string of 
characters that allows for one mismatch/deletion
within the middle of the almost-palindrome.
'''

# ------------------------------------------------------------
# Function: wannabe_palindrome
# Input: s (str) → the string we’re checking
# Output: int → the length of the longest wannabe palindrome
# Notes:
#   - "def" means we are defining a new function
#   - "s: str" is a type hint, saying the input is a string
#   - "-> int" is another type hint, saying the output is an integer
# ------------------------------------------------------------
# could do like this def wannabe_palindrome(s: str) -> int:
#but the assingnment requires this
# ------------------------------------------------------------
# Function Name: wannabe_palindrome
# Input: s → the input string
# Output: the length of the longest wannabe palindrome (integer)
# ------------------------------------------------------------
def wannabe_palindrome(s):
    """
    Return the length of the longest 'wannabe palindromic' substring.

    Rules enforced:
      - At most one interior fault (one mismatched pair OR one deletion).
      - The fault may not land at the final ends of the substring.
      - If we delete a character, it does not count toward the length.
    """
    n = len(s)
    if n <= 1:
        return n

    def expand_best(l0, r0):
        # used_fault: already spent our one allowance (mismatch OR deletion)
        # used_deletion: specifically, we chose a deletion on this path
        def expand(l, r, used_fault, used_deletion):
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    continue

                if used_fault:
                    break  # no allowance left

                # --- Option 1: treat this as one mismatched pair (no deletion) ---
                current_len = r - l + 1
                len_mismatch = expand(l - 1, r + 1, True, used_deletion=False)
                # Only accept if we grew beyond this pair so the mismatch is interior
                if len_mismatch <= current_len:
                    len_mismatch = 0

                # --- Option 2: delete/skip the left character ---
                len_skip_left = expand(l - 1, r, True, used_deletion=True)

                # --- Option 3: delete/skip the right character ---
                len_skip_right = expand(l, r + 1, True, used_deletion=True)

                return max(len_mismatch, len_skip_left, len_skip_right)

            # Done expanding; compute length of the kept window
            base_len = r - l - 1
            if used_deletion and base_len > 0:
                base_len -= 1  # remove the deleted char
            if base_len < 0:
                base_len = 0
            return base_len

        return expand(l0, r0, used_fault=False, used_deletion=False)

    best = 1
    for i in range(n):
        best = max(best, expand_best(i, i))       # odd
        if i + 1 < n:
            best = max(best, expand_best(i, i+1)) # even
    return best

if __name__ == "__main__":
    tests = {
        "abcba": 5,
        "abcbda": 6,
        "abcd": 1,
        "abbad": 4,
        "aabdcbaakkk": 8,
        "a": 1,
        "aa": 2,
        "aba": 3,
        "abca": 4,   # ← corrected
        "xbayabz": 5,
    }
    for s0, want in tests.items():
        got = wannabe_palindrome(s0)
        print(f"{s0!r} -> {got}  ({'OK' if got == want else 'expected ' + str(want)})")

        print("aabacaaa ->", wannabe_palindrome("aabacaaa"))  # should print 7
        print("aabacaaa ->", wannabe_palindrome("aabacaaa"))  # should print 7

        print(wannabe_palindrome("aabacaaa"))  # should be 7
print(wannabe_palindrome("abca"))      # should be 4 (one interior mismatch)