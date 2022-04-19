import re
import nltk
import json
import os
from urllib import request

def extract_text(filename):
    '''
    Extract the text from the file name (json file) and
    index the content from paper_id, title, abstract and body_text fields
    Retunrs - text of title, abstract and bodt_text
    '''

    file = open(filename,'rb')
    body_text = ""
    abstract = ""
    title = ""
    paper_id = ""

    paper_content = json.load(file)

    #get the paper_id
    if 'paper_id' in paper_content:
        paper_id = paper_content['paper_id']
        
    #get the title, if available
    if 'title' in paper_content['metadata']:
        title = paper_content['metadata']['title']
    #get abstract.text, if available
    if 'abstract' in paper_content:
        for abs in paper_content['abstract']:
            abstract = abstract + abs['text']
    if 'body_text' in paper_content:
        for bt in paper_content['body_text']:
            body_text = body_text + bt['text']


   
    return (title + ' ' + abstract + ' ' + body_text + ' ').lower()

def remove_punctuation(token):
  copy = token
  start = ''
  end = ''
  if token[0] in ['.',',']:
    start = token[0]
    copy = copy[1:]
  elif not(re.findall("[a-z0-9\+\-]",token[0])):
    copy = copy[1:]
  
  if token[-1] in ['.',',']:
    end = token[-1]
    copy = copy[:-1]
  elif not(re.findall("[a-z0-9\+\-\%\\\\]",token[-1])):
    copy = copy[:-1]
    
  return copy, start, end
           





def expand_contractions(token):
  
  '''
  Function to expand contractions if any.
  token: string
  return type: string
  '''
  try:
    f = open('contractions.json','r')
    contractions = json.load(f)
    f.close()
  except:
    response = request.urlretrieve("https://raw.githubusercontent.com/oshita30/contractions/main/contractions.json", "contractions.json")
    f = open('contractions.json','r')
    contractions = json.load(f)
    f.close()
    
  if "'" in token:
    try:
      return contractions[token][0]
    except KeyError:
      return token
  else:
    return token
  
  
  
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
  token: string
  stpwrds: '' if stopword else token
  return type: string
  '''
  
  if token in stpwrds:
    return ''
  else:
    return token

  
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


def preprocess(token):
  '''
  returns expanded contractions and lemmatized word
  token: string
  return type: string
  '''
  expanded = expand_contractions(token)
  if ' ' in expanded:
    cont = True
  
  if not(cont):
    lem_token = lemmatize(expanded)
    
  return lem_token, cont
  


def tokenizer_counter(text):
  text = text.strip() + ' '
  list_of_words = []
  token = ''
  for s in text:
    if s.strip() == '':
      # process "token"
      if token == '':
        continue
      token = token.lower()
      
      token, start, end = remove_punctuation(token)
      # token at this point is a word without punctuation at start or end
      token, cont = preprocess(token)
      if start:
        list_of_words.append(start)
      list_of_words.append(token)
      if end:
        list_of_words.append(end)
      if cont:
        token =''
        continue
      else:
        token = remove_stopwords(token)
        token = remove_emailURL(token)
        try:
          word_count[token] += 1
        except KeyError:
          word_count[token] = 1
        token = ''
    else:
      token = token + s
      
    return list_of_words
     
    
def read_args():
    parser = argparse.ArgumentParser()    
    parser.add_argument('-input_json_path', type=str, default='./pdf_json', help='the directory of our json data')
    parser.add_argument('-list_of_words_output_path', type=str, default='./json_list_of_words', help='the directory of our output data')
    return parser    
    
if __name__ == "__main__":
  params = read_args().parse_args()
  global word_count
  word_count = {}
  lop = os.listdir(params.input_json_path)
  for filename in lop:
    if filename[-4:].lower() == 'json':
      text = extract_text(filename)
      list_of_words = tokenizer_counter(text)
      filename = filename[:-4] + '.json'
      f = open(params.list_of_words_output_path+'/'+filename,'wb')
      f.write(json.dumps(list_of_words))
      f.close()
  
  jsonFile = open("word_count.json", "w")
  jsonFile.write(json.dumps(word_count))
  jsonFile.close()
    
