def get_word_length(text):
  return len(text.split())

def get_character_lengths(text):
  words = text.split()
  lengths = {}

  for word in words:
    for char in word:
      lowercase_char = char.lower()

      if lowercase_char.isalpha():
        if lowercase_char in lengths:
          lengths[lowercase_char] += 1
        else:
          lengths[lowercase_char] = 1
  return lengths

def print_character_lengths(lengths_dict):
  lengths_list = []

  for key, value in lengths_dict.items():
    length_dict = { "letter": key, "count": value }
    lengths_list.append(length_dict)
  
  lengths_list.sort(reverse=True, key=lambda dict:dict["count"])
  for item in lengths_list:
    letter = item["letter"]
    count = item["count"]
    print(f"{letter}: {count}")