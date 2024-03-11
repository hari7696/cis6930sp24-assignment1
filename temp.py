# def merge_overlapping_substrings(substrings):
#     # Sort the substrings by their start index
#     substrings.sort(key=lambda x: x[0])

#     merged_substrings = []
#     current_start, current_end, current_substr = substrings[0]

#     for start, end, substr in substrings[1:]:
#         # Check if the current substring overlaps with the next one
#         if start <= current_end:
#             # Merge the overlapping substrings
#             current_end = max(current_end, end)
#             current_substr = substr if len(substr) > len(current_substr) else current_substr
#         else:
#             # Add the non-overlapping substring to the list
#             merged_substrings.append((current_start, current_end, current_substr))
#             current_start, current_end, current_substr = start, end, substr

#     # Add the last substring to the list
#     merged_substrings.append((current_start, current_end, current_substr))

#     return merged_substrings

# # Example usage
# date_substrings = [(12, 26, 'April 17  2024'), (28, 33, 'Today'), (37, 59, 'Sunday  April 17  2024'), (92, 101, '4/17/2024'), (120, 130, '2022-04-17'), (135, 152, 'the 17th of April'), (12, 20, 'April 17'), (45, 53, 'April 17'), (92, 101, '4/17/2024'), (120, 130, '2022-04-17')]
# merged_substrings = merge_overlapping_substrings(date_substrings)

# print(merged_substrings)

# import re

# # The regular expression pattern
# pattern = r'\b(?!(?:\+?\d{1,3}[-.\s]?)?(?:19[5-9]\d|20[0-2]\d))((?:\+?\d{1,3}[-.\s]?)?(?:\(\d{1,4}\)|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,4}(?:[-.\s]?\d{1,4})?)(?<!19[5-9]\d|20[0-2]\d)\b'
# # Sample text
# text = """The date is April 17  2024.
# Today is Sunday  April 17  2024.
# I didn't know you birthday was 4/17/2024.
# What happened on 2022-04-17?
# On the 17th of April."""

# # Find all matches in the text
# for match in re.finditer(pattern, text):
#     #if len(match.group()) > 7:
#     print((match.start(),match.end(),  match.group()))

def merge_overlapping_substrings(substrings):
    def merge_once(substrings):
        substrings.sort(key=lambda x: x[0])
        merged_substrings = []
        current_start, current_end, current_substr = substrings[0]

        for start, end, substr in substrings[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
                current_substr = substr if len(substr) > len(current_substr) else current_substr
            else:
                merged_substrings.append((current_start, current_end, current_substr))
                current_start, current_end, current_substr = start, end, substr

        merged_substrings.append((current_start, current_end, current_substr))
        return merged_substrings

    # Merge substrings until no further merges are possible
    while True:
        merged_substrings = merge_once(substrings)
        if len(merged_substrings) == len(substrings):
            break
        substrings = merged_substrings

    return merged_substrings

# Example usage
substrings = [(12, 26, 'April 17  2024'), (28, 33, 'Today'), (37, 59, 'Sunday  April 17  2024'), (92, 101, '4/17/2024'), (120, 130, '2022-04-17'), (135, 152, 'the 17th of April'), (12, 20, 'April 17'), (45, 53, 'April 17'), (92, 101, '4/17/2024'), (120, 130, '2022-04-17')]
merged_substrings = merge_overlapping_substrings(substrings)
print(merged_substrings)
