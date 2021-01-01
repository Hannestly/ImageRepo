import tensorflow.keras as keras
import tensorflow as tf
import numpy as np

def classify(image_path):
    model = keras.models.load_model("./FruitModel")
    img_height = 100
    img_width = 100
    class_names = ['Apple', 'Apricot', 'Avocado', 'Banana', 'Blueberry', 'Cherry', 'Kiwi', 'Lemon', 'Peach', 'Plum', 'Raspberry', 'Tomato']
    # apple_url = r"C:\Users\hannest\project\fruit\fruits-360\Test\Avocado\7_100.jpg"
    img = keras.preprocessing.image.load_img(image_path,target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array,0)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return class_names[np.argmax(score)]
    # print(
    #     "This image most likely belongs to {} with a {:.2f} percent confidence."
    #     .format(class_names[np.argmax(score)], 100 * np.max(score))
    # )