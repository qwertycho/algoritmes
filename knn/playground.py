import sys
import builder

maker = builder.Builder()

model = maker.load_model("model")
print("Prediction: " + model.get_prediction(model.make_item_from_dir(sys.argv[1]), 3))

import os
import json
json_data = None
with open(os.path.join("predict", sys.argv[1] ), 'r') as f:
   json_data = json.load(f)
print(json_data.get("name"))