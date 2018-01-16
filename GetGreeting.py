import time

# print the greeting and project infos
def printInfo(progName, version, author):

  cwidth = 50
  first_last = "".ljust(cwidth, "*")
  padding = "**".ljust(cwidth-2, " ")+"**"
  greeting1 = "Willkommen zu " + progName
  greeting2 = "Version: " + version + " vom " + time.strftime("%d.%m.%Y")
  greeting3 = "Entwickelt von " + author
  format_string = "**{{0:^{0}}}**".format(cwidth-4)
  
  print(first_last)
  print(padding)
  print(format_string.format(greeting1))
  print(format_string.format(greeting2))
  print(format_string.format(greeting3))
  print(padding)
  print(first_last + "\n")
