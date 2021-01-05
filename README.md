# Image Repository
## Image Repository system 
Image repository to upload the image, classify the image and view the images stored in the database. 

![main page](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/dashboard.png)

## Tools used:
- Django 
- SQL
- Tensorflow

## Key features

### Extensive search
Images can be searched in 3 ways:
1. Combined search - text input is matched to image title, description and the tag
![combined search](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/combined_search.png)        

2. Detailed search - search by image title, tag or description individually 
![detailed search](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/detailed_search.png)        

3. Search by image - upload an image to search using Tensorflow model
![search via image](https://github.com/Hannestly/ImageRepo/blob/master/screenshots/search_via_image.png)

### Automatic tag generation
When uploading image, the repository system automatically assigns a tag based on the image uploaded using Tensorflow
