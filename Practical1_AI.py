print("Hello,I'm ROBO Cleaner 🤖\nI'll help you to clean your room👍!!")
spots = ['🤢 ','🤢 ','✨ ','🤢 ','🤢 ','✨ ','✨ ','🤢 ']

def room(pic):
  pics = ""
  for i in pic:
    pics += i
  return pics
print(room(spots))


def clean(all_spot):
  cleaned =[]
  for all_spots in spots:
    if(spots == '🤢 '):
      return '✨ '
    else:
      return '✨ '

for i in range(len(spots)):
    print(clean(spots[i]), end="")
print("\nWoahh 🥳!! Your Room is clean now✨")

