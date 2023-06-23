class item():
    def __init__(self, label, features):
        self.label = label
        self.features = features
        
    def __str__(self):
        return "Label: " + self.label + " Features: " + self.features
    
def get_distance(item1, item2):
    distance = 0
    for i in range(len(item1.features)):
        distance += (item1.features[i] - item2.features[i])**2
    return distance

def get_nearest_neighbours(item, train_set, k):
    distances = []
    for train_item in train_set:
        distance = get_distance(item, train_item)
        distances.append((distance, train_item))
    distances.sort(key=lambda tup: tup[0])
    return distances[:k]

def get_prediction(neighbours):
    labels = []
    for neighbour in neighbours:
        labels.append(neighbour[1].label)
        print(neighbour[1].label)
    return max(set(labels), key=labels.count)