with open("states.txt", "r") as states_file:
  states = states_file.read() 

def textfile_to_string(filename):
  with open (filename, "r") as text_file:
    text = text_file.read()
  return text
    
    
