import sys
import builder

maker = builder.Builder()

model = maker.load_model("model")
print("Prediction: " + model.get_prediction(model.make_item_from_dir(sys.argv[1]), 3))
print("Prediction from distance: " + model.get_prediction_from_distance(model.make_item_from_dir(sys.argv[1])))


import os
import json
json_data = None
with open(os.path.join("predict", sys.argv[1] ), 'r') as f:
   json_data = json.load(f)
print("actual: " + str(json_data.get("name")))