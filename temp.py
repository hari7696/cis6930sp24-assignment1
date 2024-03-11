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

import re

# The regular expression pattern
pattern = r"\b(?:(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4})|(?:\d{2,4}[-/.]\d{1,2}[-/.]\d{1,2})|(?:\d{2,4}[-/.]\d{1,2})|(?:\d{1,2}[-/.]\d{2,4})|(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{2,4})|(?:\d{2,4}[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)|(?:\d{1,2}(?:st|nd|rd|th)?[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{2,4})|(?:\d{2,4}[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{1,2}(?:st|nd|rd|th)?)|(?:\d{1,2}[-/.]\d{1,2})|(?:\d{1,2}(?:st|nd|rd|th)?[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)|(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{1,2}(?:st|nd|rd|th)?)|(?:\d{2,4}[-/.]\d{1,2})\b)(?:\s+(\d{1,2}:\d{2}(?::\d{2})?\s?(?:AM|PM)?\s?(?:UTC|GMT|[A-Z]{1,4}|(?:[A-Z][a-z]+(?:_|\s)?)+)[+-]?(?:\d{1,2}:\d{2}|\d{1,2})?))?"
# Sample text
text = """This is mailid hari.golamari@gmail.com and  I born on 12/12/1990 this is my phone number 8333087809 jan 2022,"""

from dateparser.search import search_dates
dates = search_dates(text, settings={'STRICT_PARSING': False})
print(dates)
for date in dates:
    search_key = date[0]
    # Create a regular expression pattern that allows for variable whitespace
    pattern = re.compile(r'\s*'.join(re.escape(word) for word in search_key.split()))
    for match in pattern.finditer(text):
        print(match.start(), match.end(), match.group())

# # Find all matches in the text
# for match in re.finditer(pattern, text):
#     #if len(match.group()) > 7:
#     print((match.start(),match.end(),  match.group()))




# def merge_overlapping_substrings(substrings):
#     def merge_once(substrings):
#         substrings.sort(key=lambda x: x[0])
#         merged_substrings = []
#         current_start, current_end, current_substr = substrings[0]

#         for start, end, substr in substrings[1:]:
#             if start <= current_end:
#                 current_end = max(current_end, end)
#                 current_substr = substr if len(substr) > len(current_substr) else current_substr
#             else:
#                 merged_substrings.append((current_start, current_end, current_substr))
#                 current_start, current_end, current_substr = start, end, substr

#         merged_substrings.append((current_start, current_end, current_substr))
#         return merged_substrings

#     # Merge substrings until no further merges are possible
#     while True:
#         merged_substrings = merge_once(substrings)
#         if len(merged_substrings) == len(substrings):
#             break
#         substrings = merged_substrings

#     return merged_substrings

# # Example usage
# substrings = [(12, 26, 'April 17  2024'), (28, 33, 'Today'), (37, 59, 'Sunday  April 17  2024'), (92, 101, '4/17/2024'), (120, 130, '2022-04-17'), (135, 152, 'the 17th of April'), (12, 20, 'April 17'), (45, 53, 'April 17'), (92, 101, '4/17/2024'), (120, 130, '2022-04-17')]
# merged_substrings = merge_overlapping_substrings(substrings)
# print(merged_substrings)
