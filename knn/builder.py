class knn:
    shape_width = 0
    shape_height = 0 
    knn_model = None
    dataset_dir = ""
    
    def __init__(self) -> None:
        pass
    
    def shape(self, width, height):
        if self.shape_height == 0 and self.shape_width == 0:
            self.shape_width = width
            self.shape_height = height
        else:
            raise Exception("input shape already defined!")
    
    def data_dir(self, dir):
        self.data_dir = dir

    def load_dataset(self, dir):
        import os
        import json
        json_data = []
        for file in os.listdir(dir):
            if file.endswith(".json"):
                with open(os.path.join(dir, file), 'r') as f:
                    json_data.append(json.load(f))
        return self.convert_json_to_item(json_data)
    
    def convert_json_to_item(self, data):
        items = []
        for object in data:
            label = object.get("name")
            shape = object.get("data")
            if not shape == None and not label == None:
                items.append(Item(label, shape))
            else:
                print("Item did not have label or shape!")
        return items
    
    def make_model(self):
        if self.knn_model == None:
            self.knn_model = Model(self.shape_width, self.shape_height, self.load_dataset(self.data_dir))
            return self.knn_model
        else:
            raise Exception("Model already built")
    
    def get_model(self):
        return self.knn_model

class Model:
    shape_width = 0
    shape_height = 0
    dataset = []
   
    def __init__(self, width, height, dataset) -> None:
        self.shape_width = width
        self.shape_height = height
        self.dataset = dataset
        
    def get_distance(self, item1, item2):
        distance = 0
        for i in range(len(item1.features)):
            distance += (item1.features[i] - item2.features[i])**2
        return distance

    def get_nearest_neighbours(self, item, k):
        distances = []
        for train_item in self.dataset:
            distance = self.get_distance(item, train_item)
            distances.append((distance, train_item))
        distances.sort(key=lambda tup: tup[0])
        return distances[:k]

    def get_prediction(self, neighbours):
        labels = []
        for neighbour in neighbours:
            labels.append(neighbour[1].label)
        return max(set(labels), key=labels.count)

class Item():
    def __init__(self, label, features):
        self.label = label
        self.features = features
        
    def __str__(self):
        return "Label: " + self.label + " Features: " + self.features