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