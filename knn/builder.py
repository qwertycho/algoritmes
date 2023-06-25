from modelClass import Model
from modelClass import Item
from aligners import Aligners

class Builder:
    
    shape_width = 0
    shape_height = 0 
    knn_model = None
    dataset_dir = ""
    train_datadir = ""
    _aligners = Aligners()        
    
    #flags
    _mem_model = True
    _ret_on_load = True
    _print_output = True
    
    def __init__(self) -> None:
        pass
    
    def shape(self, width, height):
        '''
        set the shape of the object
        '''
        if self.shape_height == 0 and self.shape_width == 0:
            self.shape_width = width
            self.shape_height = height
        else:
            raise Exception("input shape already defined!")
    
    def data_dir(self, dir):
        '''
        set the directory where all .json files should be loaded from
        '''
        self.data_dir = dir
        
    def train_dir(self, dir):
        self.train_datadir = dir  

    def make_model(self) -> Model:
        '''
        build the model and return it \n
        keeps the model in memory if the _mem_model flag is set
        '''
        model = Model(width=self.shape_width, 
                      height=self.shape_height, 
                      dataset=self._load_dataset(self.data_dir),
                      aligners = self._aligners,
                                         )
            
        if self._mem_model:
            self.knn_model = model
            
        return model 
    
    def save_model(self, path):
        '''
        save the model to a file as a pickle object
        '''
        import pickle
        with open(path, 'wb') as f:
            pickle.dump(self.knn_model, f)
    
    def load_model(self, path) -> Model:
        '''
        load a model from a file and return it if the _ret_on_load flag is set
        '''
        import pickle
        with open(path, 'rb') as f:
            self.knn_model = pickle.load(f)
        
        if self._ret_on_load:
            return self.knn_model
        
    def fit(self, epochs = 5, model = None):
        '''
        fit the model to the train data \n
        epochs: amount of times the model should be trained on the train data \n
        epochs are used to find the ideal k value by comparing the score of the previous epoch with the current epoch \n
        epochs are the upper limit of the ideal k value \n
        if no model is given the model that is in memory will be used
        '''
        if model == None:
            model = self.knn_model
            
        train_data = self._load_dataset(self.train_datadir)
        
        score = 0 
        highscore = 0
        ideal_k = epochs 
        
        new_k = 0
                
        for new_k in range(epochs):
            new_k += 1
            score = 0
            
            print("Epoch: " + str(new_k))
            for item in train_data:
                prediction = model.get_prediction(item, ideal_k)
                if prediction == item.label:
                    score += 1
            
            if score > highscore:
                ideal_k = new_k
                highscore = score
                if self._print_output:
                    print("score: " + str(score) + " at K: " + str(new_k))
            
            model._ideal_k = ideal_k
            
            if self._mem_model:
                self.knn_model = model
        
        if self._print_output:
            print("new high score: " + str(highscore) + " at ideal K: " + str(ideal_k))
    
    def fit_from_distance(self, epochs = 100, model = None):
        if model == None:
            model = self.knn_model
            
        train_data = self._load_dataset(self.train_datadir)
        
        score = 0 
        highscore = 0
        ideal_radius = 0 
        
        for new_radius in range(epochs +1):
            score = 0
            
            print("Epoch: " + str(new_radius))
            for item in train_data:
                try:
                    prediction = model.get_prediction_from_distance(item, new_radius)
                    if prediction == item.label:
                        score += 1
                except:
                    if  self._print_output:
                        print("no prediction at k: " + str(new_radius))
                    score = 0
            
            if score > highscore:
                ideal_radius = new_radius
                highscore = score
                if self._print_output:
                    print("score: " + str(score) + " at K: " + str(new_radius))
            
            model._ideal_radius = ideal_radius
            
            if self._mem_model:
                self.knn_model = model
        
        if self._print_output:
            print("New high score: " + str(highscore) + " at ideal radius: " + str(ideal_radius))
            

    def _load_dataset(self, dir):
        '''
        load all *.json files from the data_dir and convert them into Items
        '''
        import os
        import json
        json_data = []
        for file in os.listdir(dir):
            if file.endswith(".json"):
                with open(os.path.join(dir, file), 'r') as f:
                    json_data.append(json.load(f))
        return self._convert_json_to_item(json_data)
    
    def _convert_json_to_item(self, data):
        items = []
        for object in data:
            label = object.get("name")
            shape = object.get("data")
            if not shape == None and not label == None:
                if not len(shape) == self.shape_width * self.shape_height:
                    return Exception("Shape is not the same size as the input shape!")
                shape = self._aligners.align_top(vector = shape, width = self.shape_width, height = self.shape_height)
                shape = self._aligners.align_left(vector = shape, width = self.shape_width, height = self.shape_height)
                items.append(Item(label, shape))
            else:
                print("Item did not have label or shape!")
        return items