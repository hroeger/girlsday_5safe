from girls_day import GirlsDayModel
import pickle

X = [[1,1],[1,1], [1,0], [1,0], [0,0],[0,1],[1,1], [0,1], [0,0], [0,0]] #true, true, false, false, false, false, true, false ,false
y = [1,1,1,0,0,0,0,1,0,0]

clf, path =GirlsDayModel.train_model(X,y)

with open(path,'rb') as f:
    clf = pickle.load(f)

print(clf.predict([[1,1]]))
print(clf.predict([[1,0]]))
print(clf.predict([[0,0]]))
print(clf.predict([[0,1]]))
