def is_funny_string(s):
    reversed_s = s[::-1]
    for i in range(1, len(s)):
        original_diff = abs(ord(s[i]) - ord(s[i-1]))
        reversed_diff = abs(ord(reversed_s[i]) - ord(reversed_s[i-1]))
        if original_diff != reversed_diff:
            return "Not Funny"
    return "Funny"