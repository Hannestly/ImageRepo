# Image Repository
## Image Repository system 
Image repository to upload the image, classify the image and view the images stored in the database. 

![main page](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/dashboard.png)

## Tools used:
- Django 
- SQL
- Tensorflow

## Instructions to run
1. Install dependencies by running the following command in the cloned repository   
```pip install -r requirements.txt```
2. Run the Django server using the following command    
```python3 manage.py runserver```   
3. Using browser of your choice, go to ```localhost:8000``` to view the project

## Key features

### Extensive search
Images can be searched in 3 ways:
1. Combined search - text input is matched to image title, description and the tag
![combined search](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/combined_search.png)        

2. Detailed search - search by image title, tag or description individually 
![detailed search](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/detailed_search.png)        

3. Search by image - upload an image to search based on content of the image
![search via image](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/search_via_image.png)

### Automatic tag generation
When uploading image, the repository system automatically assigns a tag based on the image uploaded using Tensorflow

## Dataset used
The classification model was created using Fruit-360 dataset, an open-source dataset available on Kaggle (https://www.kaggle.com/moltean/fruits). The dataset was modified to classify between 12 different classes: 'Apple', 'Apricot', 'Avocado', 'Banana', 'Blueberry', 'Cherry', 'Kiwi', 'Lemon', 'Peach', 'Plum', 'Raspberry', 'Tomato'.   
To test out the classification yourself, there exists a folder containing test images under ```test_images``` folder. 
![test images](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/test_images.png)

