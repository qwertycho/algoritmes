import builder 
import sys

maker = builder.Builder()

maker.shape(10, 10)
maker.data_dir("dataset")
model = maker.make_model()

predict_name = sys.argv[1]
k = int(sys.argv[2])

predict_item = model.make_item_from_dir(predict_name)
predicted = model.get_prediction(predict_item, k)
print("Het is een: " +  predicted)

maker.train_dir("predict")
maker.fit(epochs = k, model = model)
maker.save_model("model")