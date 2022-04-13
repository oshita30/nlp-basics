def remove_stopwords(token,stpwrds = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost",
           "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",
           "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",
           "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand",
           "behind", "being", "below", "beside", "besides", "between", "beyond", "both", "but",
           "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "de", "describe",
           "do", "either", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere",
           "except", "few", "for", "from", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein",
           "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest",
           "into", "is", "it", "its", "itself", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
           "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine",
           "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on",
           "once", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out",
           "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "she", "should", "since", "sincere",
           "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still",
           "such", "than", "that", "the", "their", "them", "themselves", "then", "thence",
           "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they",
           "third", "this", "those", "though", "through", "throughout", "thru", "thus", "to", "together",
           "too", "toward", "towards", "un", "under", "until", "up", "upon", "us",
           "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where",
           "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while",
           "whither", "who", "whoever", "whom", "whose", "why", "will", "with", "within", "without",
           "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]):
  '''
  token: list of size 1 or 2 (2 due to contractions)
  stpwrds: list of stopwords given during function call
  return type: list
  '''
  
  if len(token)>1 or token[0] in stpwrds:
    return []
  else:
    return token
