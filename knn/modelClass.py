class Model:
    shape_width = 0
    shape_height = 0
    _ideal_k = 1
    dataset = []
   
    def __init__(self, width, height, dataset) -> None:
        self.shape_width = width
        self.shape_height = height
        self.dataset = dataset
        
    def get_prediction(self, to_predict, k = _ideal_k):
        neighbours = self._get_nearest_neighbours(to_predict, k)
        labels = []
        for neighbour in neighbours:
            labels.append(neighbour[1].label)
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