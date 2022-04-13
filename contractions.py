def contractions(token):
  
  '''
  Function to expand contractions if any.
  token: string
  return type: list
  '''
  
  f = open('contractions.json','r')
  contractions = json.load(f)
  f.close()
  if "'" in token:
    try:
      return contractions[token][0].split(' ')
    except KeyError:
      return [token]
  else:
    return [token]
