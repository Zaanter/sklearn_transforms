from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder



# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')
    
class DeleteInconsistentRows(BaseEstimator, TransformerMixin):
    def __init__(self):
        return
        
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        data = X.copy()
        
        data = data[(data['NUM_COURSES_BEGINNER_DATASCIENCE'] != 0) | (data['NUM_COURSES_ADVANCED_DATASCIENCE'] != 0) & (data['HOURS_DATASCIENCE'] != 0)]
        data = data[(data['NUM_COURSES_BEGINNER_FRONTEND'] != 0) | (data['NUM_COURSES_ADVANCED_FRONTEND'] != 0) & (data['HOURS_FRONTEND'] != 0)]
        data = data[(data['NUM_COURSES_BEGINNER_BACKEND'] != 0) | (data['NUM_COURSES_ADVANCED_BACKEND'] != 0) & (data['HOURS_BACKEND'] != 0)]
        
        data = data[(data['NUM_COURSES_BEGINNER_DATASCIENCE'] != 0) | (data['NUM_COURSES_ADVANCED_DATASCIENCE'] != 0) & (data['AVG_SCORE_DATASCIENCE'] != 0)]
        data = data[(data['NUM_COURSES_BEGINNER_FRONTEND'] != 0) | (data['NUM_COURSES_ADVANCED_FRONTEND'] != 0) & (data['AVG_SCORE_FRONTEND'] != 0)]
        data = data[(data['NUM_COURSES_BEGINNER_BACKEND'] != 0) | (data['NUM_COURSES_ADVANCED_BACKEND'] != 0) & (data['AVG_SCORE_BACKEND'] != 0)]
        
        
        return data
