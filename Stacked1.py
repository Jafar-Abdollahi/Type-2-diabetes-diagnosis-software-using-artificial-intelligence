from sklearn.model_selection import train_test_split
from mlxtend.classifier import StackingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn import datasets, metrics
import stacked_generalization
from mlxtend.classifier import StackingClassifier
from stacked_generalization import StackedGeneralizer
import pandas as pd
Diabetic=pd.read_csv('diabetes.csv')
X=Diabetic[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
y=Diabetic['Outcome']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=30,random_state=0)
# Stage 1 model
bclf = LogisticRegression(random_state=1)

# Stage 0 models
clfs = [RandomForestClassifier(n_estimators=40, criterion = 'gini', random_state=1),
        GradientBoostingClassifier(n_estimators=25, random_state=1),
        RidgeClassifier(random_state=1)]

# same interface as scikit-learn
#sl = StackedClassifier(bclf, clfs)
#sl.fit(X,y)
sl = StackingClassifier(classifiers=clfs,meta_classifier=bclf)
sl.fit(X,y)
score = metrics.accuracy_score(y, sl.predict(X))
print("Accuracy: %f" % score)
Diabetic_prediction_SL=sl.predict([[1,2,3,4,5,6,7,8]])
lookup_Diabetic_name_Stack=[Diabetic_prediction_SL[0]]

print('[Result]','Stack=',lookup_Diabetic_name_Stack)
