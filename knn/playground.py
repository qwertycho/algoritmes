import builder

maker = builder.Builder()

model = maker.load_model("model")
print("Prediction: " + model.get_prediction(model.make_item_from_dir("test.json"), 3))


import os
import json
json_data = None
with open(os.path.join("predict", "test.json"), 'r') as f:
   json_data = json.load(f)
print(json_data.get("name"))