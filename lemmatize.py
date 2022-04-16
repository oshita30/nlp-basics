def lemmatize(token):
  '''
  to lemmatize the token based on pos_tag
  
  token: string word
  return type: lemmatized string word
  '''
  

  tag = nltk.pos_tag([token])[0][1]
  lem_token = ''
  if tag[0] == 'V':
    lem_token = lemmatizer.lemmatize(token,pos='v')
  elif tag[0] == 'J':
    lem_token = lemmatizer.lemmatize(token,pos='a')
  elif tag[0] == 'R':
    try:
      lem_token = wn.synset(token+'.r.2').lemmas()[0].pertainyms()[0].name()
    except:
      lem_token = wn.synset(token+'.r.1').lemmas()[0].pertainyms()[0].name()
  else:
    lem_token = lemmatizer.lemmatize(token,pos='n')
  


  
  return lem_token
