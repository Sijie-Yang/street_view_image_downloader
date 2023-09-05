import requests
import csv
import os
from PIL import Image
from io import BytesIO

class StreetViewDownloader:
    BASE_URL = "https://maps.googleapis.com/maps/api/streetview"

    def __init__(self, api_key):
        self.api_key = api_key

    def download_image(self, lat, lng, size='640x480', fov=90, heading=0, pitch=0, radius=50, source='default', params=None, output_folder=".", panorama=False):
        if params is None:
            params = {}

        # Adding default parameters to the URL
        params['size'] = size
        params['fov'] = fov
        params['pitch'] = pitch
        params['radius'] = radius
        params['source'] = source

        if panorama:
            # If panorama is True, download and stitch images from four different headings
            imgs = []
            for heading in [0, 90, 180, 270]:
                params['heading'] = heading
                response = self._get_image_response(lat, lng, params)
                if response.status_code != 200:
                    print(f"Error downloading image for heading {heading}. Response: {response.text}")
                    return
                imgs.append(Image.open(BytesIO(response.content)))

            # Combining the four images to create a panoramic image
            total_width = sum([img.width for img in imgs])
            max_height = max([img.height for img in imgs])
            panorama_img = Image.new("RGB", (total_width, max_height))
            x_offset = 0
            for img in imgs:
                panorama_img.paste(img, (x_offset, 0))
                x_offset += img.width
            
            # Saving the panoramic image
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            panorama_img.save(os.path.join(output_folder, f"{lat}_{lng}.jpg"))
        else:
            # If panorama is False, just download a single image
            params['heading'] = heading
            response = self._get_image_response(lat, lng, params)
            if response.status_code == 200:
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                image_filename = f"{lat}_{lng}.jpg"
                with open(os.path.join(output_folder, image_filename), "wb") as f:
                    f.write(response.content)
            else:
                print(f"Error downloading image for {lat}, {lng}. Response: {response.text}")

    def _get_image_response(self, lat, lng, params):
        # Generating the URL with the given parameters
        url = f"{self.BASE_URL}?location={lat},{lng}&key={self.api_key}"
        for key, value in params.items():
            url += f"&{key}={value}"
        return requests.get(url)

    def batch_download(self, csv_file, output_folder=".", api_keys=None, images_per_key=10, panorama=False, 
                    size='640x480', fov=90, heading=0, pitch=0, radius=50, source='default', params=None):
        if api_keys is None:
            api_keys = [self.api_key]
        
        # Initial API key index
        api_key_index = 0  
        self.api_key = api_keys[api_key_index]  # Use the first API key

        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                lat = row['latitude']
                lng = row['longitude']
                    
                self.download_image(lat, lng, output_folder=output_folder, panorama=panorama, 
                                    size=size, fov=fov, heading=heading, pitch=pitch, radius=radius, source=source, params=params)
                    
                # Rename the image using a numerical sequence
                original_filename = os.path.join(output_folder, f"{lat}_{lng}.jpg")
                new_filename = os.path.join(output_folder, f"{count+1}.jpg")
                if os.path.exists(new_filename):  # If the new filename already exists, delete it first
                    os.remove(new_filename)
                if os.path.exists(original_filename):
                    os.rename(original_filename, new_filename)
                    
                count += 1
                
                # Logic to switch API keys
                if count % images_per_key == 0:
                    print(f"Downloaded {images_per_key} images with key {self.api_key}.")
                    api_key_index += 1
                    if api_key_index >= len(api_keys):
                        print(f"Reached limit of API keys (images_per_key = {images_per_key}). Adjust the value if needed.")
                        break
                    self.api_key = api_keys[api_key_index]
                    
            print(f"Downloaded {count} images in total.")

