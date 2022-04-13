def remove_stopwords(token,stpwrds):
  '''
  token: list of size 1 or 2 (2 due to contractions)
  stpwrds: list of stopwords given during function call
  return type: list
  '''
  
  if len(token)>1 or token[0] in stpwrds:
    return []
  else:
    return token
