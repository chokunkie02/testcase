def find_longest_alternating_substring(s):
    max_len = 0
    unique_chars = set(s)
    
    for first in unique_chars:
        for second in unique_chars:
            if first == second:
                continue
            filtered = [c for c in s if c == first or c == second]
            if all(filtered[i] != filtered[i+1] for i in range(len(filtered)-1)):
                max_len = max(max_len, len(filtered))
    
    return max_len