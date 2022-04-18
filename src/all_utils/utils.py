import ast                                                                                                                        #for converting str to list
import nltk
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity


class Helper:
    def __init__(self):
        self.stemmer = PorterStemmer()
        
    def convert(self, text):
        
        """
        Convert a string to a list of words.
        """
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name']) 
        return L
    
    
    def merge1(self, df1, df2):
        """
        Merge two dataframe.
        """
        df1 = df1.merge(df2,on='title')
        return df1


    def convert_cast(self, text):
        """
        Convert a string to a list of words and extract cast.
        """
        L = []
        counter = 0
        for i in ast.literal_eval(text):
            if counter < 3:                                                                                                           # Here i am just keeping top 3 cast
                L.append(i['name'])
            counter+=1
        return L


    def fetch_director(self, text):
        """_
        Convert a string to a list of words and extract director.
        """
        L = []
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
        return L


    def remove_space(self, L):
        """
        Removing space from a list. Like 'Anna Kendrick' = 'AnnaKendrick'
        """
        L1 = []
        for i in L:
            L1.append(i.replace(" ",""))
        return L1


    def stems(self, text):
        """
        Perform Stemming operation.
        """
        T = []
        
        for i in text.split():
            T.append(self.stemmer.stem(i))
        
        return " ".join(T)


    
