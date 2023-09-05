### street_view_image_downloader

The `street_view_image_downloader` package provides an easy way to download images from Google Street View, based on specified latitude and longitude. One of the highlighted features is the ability to switch between multiple API keys after a set number of images, useful for projects requiring a large number of downloads.

## Installation

```bash
pip install street_view_image_downloader
```

Before you use this package, make sure you have the following libraries installed:

```bash
pip install requests
pip install pillow
```

## Usage

### 1. Initialize the StreetViewDownloader:

```python
from street_view_image_downloader import StreetViewDownloader
api_key = "YOUR_API_KEY"
downloader = StreetViewDownloader(api_key)
```

### 2. Download a Single Image:

```python
lat, lng = 37.4219999,-122.0840575
downloader.download_image(lat, lng)
```

### 3. Download Multiple Images from a CSV:

The CSV file should have at least two columns labeled `latitude` and `longitude`.

```python
downloader.batch_download('test_data.csv', output_folder='test_images')
```

### 4. Switching Between Multiple API Keys:

If you have multiple API keys and wish to switch between them after a certain number of images:

```python
api_keys_list = ['YOUR_FIRST_API_KEY', 'YOUR_SECOND_API_KEY']
downloader.batch_download('test_data.csv', output_folder='test_images_with_keys', api_keys=api_keys_list, images_per_key=3)
```

### 5. Download Panoramic Images:

```python
downloader.download_image(lat, lng, panorama=True)
```

### 6. Batch Download of Panoramas with API Key Switching:

```python
downloader.batch_download('test_data.csv', output_folder='panorama_images_with_keys', api_keys=api_keys_list, images_per_key=3, panorama=True)
```

## Function Parameters:

- **download_image()**:
  - `lat, lng`: Coordinates for the image location.
  - `size`: Image size (default is '640x480').
  - `fov`: Field of view (default is 90).
  - `heading`: Direction of the camera (default is 0).
  - `pitch`: Vertical angle of the camera (default is 0).
  - `radius`: Defines search radius in meters (default is 50).
  - `source`: Source of image (default is 'default').
  - `params`: Additional parameters to add to the URL (default is None).
  - `output_folder`: Folder to save the image (default is the current directory).
  - `panorama`: Download and stitch images from four different headings to create a panoramic image (default is False).

- **batch_download()**:
  - `csv_file`: Path to the CSV file with `latitude` and `longitude` columns.
  - `output_folder`: Folder to save the images.
  - `api_keys`: List of API keys to switch between.
  - `images_per_key`: Number of images to download before switching to the next API key.
  - `panorama`: Download panoramic images (default is False).
  - Other parameters are the same as `download_image`.

## Example
test_data.csv
```csv
fid,longitude,latitude
"1",103.765122970844,1.30965425545428
"2",103.765021255793,1.30750431934011
"3",103.765697688518,1.30809182184852
"4",103.76394839739,1.30704156863037
"5",103.765635385026,1.30919496716719
"6",103.683405292776,1.32262405192394
"7",103.825063477163,1.27778520523892
"8",103.681608273124,1.32264114501178
"9",103.682506782935,1.32263259863189
"10",103.824646230205,1.27806244787668
```

test_downloader.py
```python
from streetview-image-downloader import StreetViewDownloader

# Initialize the StreetViewDownloader class with your API key
api_key = "YOUR_FIRST_API_KEY"
api_keys_list = ['YOUR_FIRST_API_KEY', 'YOUR_SECOND_API_KEY']  # This is for Example 3 and Example 5 for API key switching download
downloader = StreetViewDownloader(api_key)

# Example 1: Download a single image (e.g., for Googleplex)
lat, lng = 37.4219999,-122.0840575
print("Downloading single image for Googleplex coordinates...")
downloader.download_image(lat, lng)
print("Download complete.\n")

# Example 2: Download a batch of images using a CSV file without API key switching
print("Batch downloading without API key switching...")
downloader.batch_download('test_data.csv', output_folder='test_images')
print("Batch download without API key switching complete.\n")

# Example 3: Download a batch of images using a CSV file with API key switching
print("Batch downloading with API key switching...")
downloader.batch_download('test_data.csv', output_folder='test_images_with_keys', api_keys=api_keys_list, images_per_key=3)
print("Batch download with API key switching complete.\n")

# Example 4: Download a single panoramic image (e.g., for Googleplex)
print("Downloading single panoramic image for Googleplex coordinates...")
downloader.download_image(lat, lng, panorama=True)
print("Download complete.\n")

# Example 5: Batch download panoramic images with multiple API keys and switching keys after a set number of images
print("Batch downloading panoramas with API key switching...")
downloader.batch_download('test_data.csv', output_folder='panorama_images_with_keys', api_keys=api_keys_list, images_per_key=3, panorama=True)
print("Batch download of panoramas with API key switching complete.\n")

print("All operations completed successfully!")
```

## Important Note:
Ensure that your API keys have the necessary permissions and quota to access and download from Google Street View. The API key switching feature is particularly useful to distribute the load across multiple keys and stay within the quota limits.

Happy downloading!