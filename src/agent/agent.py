import nltk
nltk.download('punkt')
nltk.download('popular')
from nltk.corpus import wordnet
class Agent:
    def query(self, query) -> str:
        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it
        syns = self.synonyms(query)
        #TODO Part of speach tagging --Nathan
        query = self.pos_tag(query)
        
        #TODO: Named Entity Recognition: Recognize names given and append
        
        #TODO: COReference: Figure out if the query is about the user or their patient is talking about --Jordan C


        ##TODO??? Other things to cover our bases if it's easy

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3

        
        return query
    
    def pos_tag(self, query):
        token = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(token)
        
        return tagged

    def synonyms(self, word):
        tag = self.pos_tag(word)
        synonyms = []
        for syn_set in wordnet.synsets(word):
            for l in syn_set.lemmas():
                name = l.name().replace("_", " ")
                testTag = self.pos_tag(name)
                if testTag[0][1] == tag[0][1]:
                    name = name.lower()
                    synonyms.append(name)
        
        print(set(synonyms))

        return synonyms