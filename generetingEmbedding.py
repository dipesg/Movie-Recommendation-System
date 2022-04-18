import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess.preprocessing import Process
import logger

class Embedding:
    def __init__(self):
        # Initializing the logger object
        self.file_object = open("Logs/embedding_log.txt", 'a+')
        self.log_writer = logger.App_Logger()
        
        self.cv = CountVectorizer(max_features=5000,stop_words='english')
        self.new_df = Process().drop_columns()
        
    def vectorize(self):
        try:
            self.vector = self.cv.fit_transform(self.new_df['tags']).toarray()
            return self.vector
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the vectorize function. Error:: %s' % ex)
            raise ex
        
    def cosine_similarity(self):
        try:
            self.vectorize_array = self.vectorize()
            self.similarity = cosine_similarity(self.vectorize_array)
            return self.similarity
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the cosine_similarity function. Error:: %s' % ex)
            raise ex
        
    def recommend(self, movie):
        try:
            self.similarity = self.cosine_similarity()
            index = self.new_df[self.new_df['title'] == movie].index[0]
            distances = sorted(list(enumerate(self.similarity[index])),reverse=True,key = lambda x: x[1])
            for i in distances[1:6]:
                print(self.new_df.iloc[i[0]].title)
                
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the recommend function. Error:: %s' % ex)
            raise ex
        
    def save_model(self):
        try:
            self.similarity = self.cosine_similarity()
            pickle.dump(self.new_df,open('artifacts/movie_list.pkl','wb'))
            pickle.dump(self.similarity,open('artifacts/similarity.pkl','wb'))
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the save_model function. Error:: %s' % ex)
            raise ex   
        
        
if __name__ == '__main__':
    embed = Embedding()
    embed.save_model()

