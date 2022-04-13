def contractions(token):
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
