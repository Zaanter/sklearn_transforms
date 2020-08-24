from sklearn.base import BaseEstimator, TransformerMixin




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
    


class oversampling(BaseEstimator, TransformerMixin):
    def __init__(self):
        self

    def fit(self, X,y=None):
        return self

    def transform(self, X):
        # Primero copiamos el dataframe de entrada 'X' de entrada
        data = X.copy()

        dataA = data[data['OBJETIVO'] == 'Aceptado']
        dataA = dataA.sample(4500, replace=True)

        dataB = data[data['OBJETIVO'] == 'Sospechoso']
        dataB = dataB.sample(4500, replace=True)

        data = pd.concat([dataA,dataB])

        return data
        # Devolvemos un nuevo marco de datos sin las columnas no deseadas
