import urllib.request
import random


def rand_file_name():
    name = str(random.randint(1,1000)) + ".jpg"
    return name

def download_puppy_picture(weburl):
    new_name = rand_file_name()
    urllib.request.urlretrieve(url = weburl, filename = new_name)
    print("Your picture has been saved under {filename}".format(filename = new_name))

download_puppy_picture("http://thomas-cokelaer.info/blog/wp-content/themes/mytheme/images/headers/stars.jpg")
