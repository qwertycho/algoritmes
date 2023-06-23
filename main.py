import builder 
import sys

maker = builder.knn()

maker.shape(10, 10)
maker.data_dir("dataset")
model = maker.make_model()

predict_name = sys.argv[1]
k = int(sys.argv[2])

def read_predict_json(predict_name):
    import os
    import json
    json_data = []
    with open(os.path.join("predict", predict_name), 'r') as f:
        json_data.append(json.load(f))
    return json_data

prdict_json = read_predict_json(predict_name)
predict_item = builder.Item(prdict_json[0].get("name"), prdict_json[0].get("data"))
predicted = model.get_prediction(model.get_nearest_neighbours(predict_item, k))
print("Het is een: " +  predicted)