## Project Overview

In this project, I built a pipeline to process real-world, user-supplied images and put model into an app.
Given an image, app will predict the most likely locations where the image was taken.

### Why We're Here

Photo sharing and photo storage services like to have location data for each photo that is uploaded. With the location data, these services can build advanced features, such as automatic suggestion of relevant tags or automatic photo organization, which help provide a compelling user experience. Although a photo's location can often be obtained by looking at the photo's metadata, many photos uploaded to these services will not have location metadata available. This can happen when, for example, the camera capturing the picture does not have GPS or if a photo's metadata is scrubbed due to privacy concerns.

If no location metadata for an image is available, one way to infer the location is to detect and classify a discernable landmark in the image. Given the large number of landmarks across the world and the immense volume of images that are uploaded to photo sharing services, using human judgement to classify these landmarks would not be feasible.

In this project, my app will accept any user-supplied image as input and suggest the top k most relevant landmarks from 50 possible landmarks from across the world.


## Project Overview

#### Step 1: Create a CNN to Classify Landmarks (from Scratch)

#### Step 2: Create a CNN to Classify Landmarks (using Transfer Learning)

#### Step 3: Write Landmark Prediction Algorithm

#### Step 4: Deploy the Porject

## Dataset Info

The landmark images are a subset of the Google Landmarks Dataset v2.

## Prerequisite

opencv-python-headless==4.5.3.56
matplotlib==3.4.3
numpy==1.21.2
pillow==7.0.0
bokeh==2.1.1
torch==1.11.0
torchvision==0.12.0
tqdm==4.63.0
ipywidgets==7.6.5
livelossplot==0.5.4
pytest==7.1.1
pandas==1.3.5
seaborn==0.11.2

