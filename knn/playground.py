import builder

maker = builder.Builder()

model = maker.load_model("model")
print(model.get_prediction(model.make_item_from_dir("test.json"), 3))