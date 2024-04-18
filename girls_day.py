from sklearn import svm
from sklearn.exceptions import NotFittedError
import pickle
import requests
import threading
import queue
from datetime import datetime

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
    def train_model(X,y):
    #X = list of arrays
    #y = list that is handed over.
        
        clf = svm.SVC()
        clf.fit(X,y)
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        with open(f'trained_model_{hours}:{minutes}.pkl0','wb') as f:
            pickle.dump(clf,f)
        return clf, f'trained_model_{hours}:{minutes}.pkl0'

    def __init__(self, path_to_model):
        with open(path_to_model,'rb') as f:
            self.model = pickle.load(f)
        #self.model = svm.SVC()
        

   # def train_model(self,X,y):

   #    self.model.fit(X, y)

    def get_model(self):
        return self.model

    def test_frame(self,input_list): #expects a list of labels. [person, person bicyle...]
        people_count = (input_list.count('bicycle')) #bicycle
        motorcycle_count = input_list.count('motorcycle')
        car_count = input_list.count('person') # person

        people = 0
        motorcycle = 0
        car = 0

        

        if people_count > 0:
            people = 1
        if motorcycle_count > 0:
            motorcycle = 1
        if car_count > 0:
            car = 1


        v = [people, car] # switch to two dimensionality
        print(v, flush=True)
    #  print(clf.predict([v])[0])
        
        # if the model is not trained yet, it will always return 0.
        try:
            prediction = self.model.predict([v])[0]
        except NotFittedError:
            prediction = 0
        
        print(prediction)
        if prediction == 1:
            return True
        return False

class GDMessageHandler():
    on_url= "http://127.0.0.1:5000/api/on"
    off_url= "http://127.0.0.1:5000/api/off"

    def __init__(self):
       # self.status_ = False
        # Create a new thread
        self.q = queue.Queue()
        sending_thread = threading.Thread(target=self.await_messages, args=(self.q,), name="sending_thread") 
        # Start the thread
        sending_thread.start()

    def await_messages(self,q):
        status_ = False
        while True:
            signal = q.get()
            if signal is None:
                break
            status_ = self.send_message(signal, status_)
            print (f'current status: {status_}', flush=True)

        # queue die wartet.
 
    def send_message(self, signal, status_):
        print("if required, sending message " + str(signal), flush=True)
        if status_ != signal:
            try:
                if signal == True:
                    status_ = True
                    response = requests.post(self.on_url)
                else:
                    status_ = False
                    response = requests.post(self.off_url)
                print("Response Status Code:", response.status_code)
                print("Response Content:", response.text)
                print(status_)
            except requests.exceptions.RequestException:
                print("could not resove url")
            # Print the response status code and content

        else: 
            print("no change in status")
        return status_


#test_frame(['person', 'person', 'person', 'person','car'])
#test_frame(['person', 'person', 'person', 'person'])
#test_frame(['person', 'person', 'person', 'person','motorcycle'])


