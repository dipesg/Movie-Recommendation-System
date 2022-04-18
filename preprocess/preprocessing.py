import pandas as pd
from all_utils.utils import Helper
import logger

class Process:
    def __init__(self):
        self.helper = Helper()
        self.movie = pd.read_csv('data/movies.csv')
        self.credits = pd.read_csv('data/credits.csv')
        
        # Initializing the logger object
        self.file_object = open("Logs/preprocessing_log.txt", 'a+')
        self.log_writer = logger.App_Logger()
        
        
    def merge_dataframe(self):
        try:
            self.first_dataframe = self.helper.merge1(self.movie, self.credits)
            return self.first_dataframe
    
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the merge_dataframe function!! Error:: %s' % ex)
            raise ex
    
    def select_columns(self):
        try:
            self.merged_dataframe = self.merge_dataframe()
            
            # Keeping important columns for recommendation
            self.merged_dataframe = self.merged_dataframe[['movie_id','title','overview','genres','keywords','cast','crew']]
            return self.merged_dataframe
            
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the select_columns function. Error:: %s' % ex)
            raise ex
            
            
    def drop_outliers(self):
        try:
            self.selected_dataframe = self.select_columns()
            
            # We have seen from our analysis there is 3 outlier in overview column, so we are dropping them.
            self.first_dataframe.dropna(inplace=True)
            return self.first_dataframe
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the drop_outliers function!! Error:: %s' % ex)
            raise ex
        
    
    def convert_to_list(self):
        try:
            self.cleaned_dataframe = self.drop_outliers()
            
            # Converting genres column to list of words
            self.cleaned_dataframe['genres'] = self.cleaned_dataframe['genres'].apply(self.helper.convert)
            #return self.movies
            
            # Converting keywords column to list of words
            self.cleaned_dataframe['keywords'] = self.cleaned_dataframe['keywords'].apply(self.helper.convert)
            
            # Converting cast column to list of words
            self.cleaned_dataframe['cast'] = self.cleaned_dataframe['cast'].apply(self.helper.convert_cast)
            
            # Fetching director name from crew column.
            self.cleaned_dataframe['crew'] = self.cleaned_dataframe['crew'].apply(self.helper.fetch_director)
            
            return self.cleaned_dataframe
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the convert_to_list function!! Error:: %s' % ex)
            raise ex
    
    
    
    def remove_space(self): 
        try:   
            self.converted_to_list_dataframe = self.convert_to_list()
        
            # Removing space from cast, crew, genres and keywords column.
            self.converted_to_list_dataframe['cast'] = self.converted_to_list_dataframe['cast'].apply(self.helper.remove_space)
            self.converted_to_list_dataframe['crew'] = self.converted_to_list_dataframe['crew'].apply(self.helper.remove_space)
            self.converted_to_list_dataframe['genres'] = self.converted_to_list_dataframe['genres'].apply(self.helper.remove_space)
            self.converted_to_list_dataframe['keywords'] = self.converted_to_list_dataframe['keywords'].apply(self.helper.remove_space)
            
            return self.converted_to_list_dataframe
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the remove_space function Error:: %s' % ex)
            raise ex
        
    
    def concat_all(self):
        try:
            self.space_removed_dataframe = self.remove_space()
            
            # Concatinate all
            self.space_removed_dataframe['tags'] = str(self.space_removed_dataframe['overview']) + str(self.space_removed_dataframe['genres']) + str(self.space_removed_dataframe['keywords']) + str(self.space_removed_dataframe['cast']) + str(self.space_removed_dataframe['crew'])
            return self.space_removed_dataframe
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the concat_all function. Error:: %s' % ex)
            raise ex
        
    def drop_columns(self):
        try:
            self.new_dataframe = self.concat_all()
            
            # Selecting only required columns and creating a new dataframe.
            self.new_dataframe = self.new_dataframe[['movie_id','title','tags']]
            return self.new_dataframe
            
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the drop_columns function. Error:: %s' % ex)
            raise ex
            
if __name__ == '__main__':
    process = Process()
    process.drop_columns()
        