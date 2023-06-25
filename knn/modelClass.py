class Model:
    shape_width = 0
    shape_height = 0
    _ideal_k = 1
    _ideal_radius = 1
    dataset = []
    _aligners = None
   
    def __init__(self, width, height, dataset, aligners = None ) -> None:
        self.shape_width = width
        self.shape_height = height
        self.dataset = dataset
        self._aligners = aligners

    def get_prediction(self, to_predict, k = _ideal_k) -> str:
        '''
        get the prediction from the k nearest neighbours (int) \n
        '''
        to_predict.features = self._aligners.align_top(vector=to_predict.features, width=self.shape_width, height=self.shape_height)
        to_predict.features = self._aligners.align_left(vector=to_predict.features, width=self.shape_width, height=self.shape_height)
        neighbours = self._get_nearest_neighbours(to_predict, k)
        labels = []
        for neighbour in neighbours:
            labels.append(neighbour[1].label)
        return max(set(labels), key=labels.count)
    
    def get_prediction_from_distance(self, to_predict, dinstance = _ideal_radius) -> str:
        '''
        get the prediction from all neighbours in a given radius (int)
        '''
        to_predict.features = self._aligners.align_top(vector=to_predict.features, width=self.shape_width, height=self.shape_height)
        to_predict.features = self._aligners.align_left(vector=to_predict.features, width=self.shape_width, height=self.shape_height)
        neighbours = self._get_neighbours_in_radius(to_predict, dinstance)
        labels = []
        for neighbour in neighbours:
            labels.append(neighbour.label)
        return max(set(labels), key=labels.count)

    def make_item_from_dir(self, name, dir = "predict"):
        import os
        import json
        json_data = None
        with open(os.path.join("predict", name), 'r') as f:
           json_data = json.load(f)
        return Item(json_data.get("name"), json_data.get("data"))
    
    def _get_distance(self, item1, item2):
        distance = 0
        for i in range(len(item1.features)):
            distance += (item1.features[i] - item2.features[i])**2
        return distance

    def _get_neighbours_in_radius(self, item, radius):
        neighbours = []
        for train_item in self.dataset:
            distance = self._get_distance(item, train_item)
            if distance <= radius:
                neighbours.append(item)
        return neighbours 

    def _get_nearest_neighbours(self, item, k):
        distances = []
        for train_item in self.dataset:
            distance = self._get_distance(item, train_item)
            distances.append((distance, train_item))
        distances.sort(key=lambda tup: tup[0])
        return distances[:k]


class Item():
    def __init__(self, label, features):
        self.label = label
        self.features = features
        
    def __str__(self):
        return "Label: " + self.label + " Features: " + self.features