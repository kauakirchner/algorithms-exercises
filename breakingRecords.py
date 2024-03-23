# Input -> 3 4 21 36 10 28 35 5 24 42
# First Score -> 3
# Times the Max Record was broked -> 4 -> 21 -> 36 -> 42 Total -> 4 times
# Times the Min Record was broked -> Never in this Input
# Output -> 4 0

def breaking_records(scores):
  times_maria_broke_her_max_record = 0
  times_maria_broke_her_min_record = 0
  current_max_record = scores[0]
  current_min_record = scores[0]

  for score in range(1, len(scores)):
    if scores[score] > current_max_record:
      times_maria_broke_her_max_record += 1
      current_max_record = scores[score]
    elif scores[score] < current_min_record:
      times_maria_broke_her_min_record += 1
      current_min_record = scores[score]
    
  return times_maria_broke_her_max_record, times_maria_broke_her_min_record


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
# Output must be -> 2 4

print(breaking_records(scores=scores))