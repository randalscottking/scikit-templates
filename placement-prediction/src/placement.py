import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


df=pd.read_csv("/kaggle/input/placement-prediction-dataset/placementdata.csv")
df=df.drop("StudentID",axis=1)
df.head()

df=pd.get_dummies(df,columns=["ExtracurricularActivities","PlacementTraining"],drop_first=True)
y=df["PlacementStatus"]
x=df.drop("PlacementStatus",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.78,random_state=66)

model=RandomForestClassifier()
model.fit(x_train,y_train)
model.score(x_test,y_test)


modellog=LogisticRegression()
modellog.fit(x_train,y_train)
modellog.score(x_test,y_test)
