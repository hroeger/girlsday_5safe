from sklearn import svm
from sklearn.exceptions import NotFittedError
import pickle
X = [[1,1,0], [1,0,1], [0,1,0],[0,1,1],[1,1,1],[0,0,0],[1,0,0],[0,0,0]]
y = [1,1,0,0,1,0,0,0]

#print(clf.predict([[1,0,0]]))
#print(clf.predict([[0,0,0]]))
#print(clf.predict([[0,1,0]]))
#print(clf.predict([[1,0,1]]))
#SVC()p


# helper  to store an empty model. executed at import. #
#clf = svm.SVC()
#with open('empty_model.pkl','wb') as f:
#    pickle.dump(clf,f)

# end helper 

class GirlsDayModel():
    def __init__(self, path_to_model):
        with open(path_to_model,'rb') as f:
            self.model = pickle.load(f)
        #self.model = svm.SVC()
        

    def train_model(self,X,y):

        self.model.fit(X, y)

    def get_model(self):
        return self.model

    def test_frame(self,input_list): #expects a list of labels.
        people_count = (input_list.count('person'))
        motorcycle_count = input_list.count('motorcycle')
        car_count = input_list.count('car')

        people = 0
        motorcycle = 0
        car = 0

        

        if people_count > 0:
            people = 1
        if motorcycle_count > 0:
            motorcycle = 1
        if car_count > 0:
            car = 1


        v = [people, motorcycle, car] #create vector to test. does it work if count > 0 or not? not really. 
    #  print(v)
    #  print(clf.predict([v])[0])
        
        # if the model is not trained yet, it will always return 0.

        # now, let's train the model.
        try:
            prediction = self.model.predict([v])[0]
        except NotFittedError:
            prediction = 0
        return prediction


#test_frame(['person', 'person', 'person', 'person','car'])
#test_frame(['person', 'person', 'person', 'person'])
#test_frame(['person', 'person', 'person', 'person','motorcycle'])
