# this will store all the detect files format in hash set

def fileformat(extension, format):
    return format[extension]


formatSet = {
    'aif': 'Audio',
    'cda': 'Audio',
    'mp3': 'Audio',
    'mpa': 'Audio',
    'ogg': 'Audio',
    'wav': 'Audio',
    'wma': 'Audio',

    '7Z': 'Compressed',
    'pkg': 'Compressed',
    'zip': 'Compressed',
    'rar': 'Compressed',
    'tag.gz': 'Compressed',
    'bin': 'Compressed',
    'dmg': 'Compressed',
    'iso': 'Compressed',

    'ai': 'Image',
    'bmp': 'Image',
    'svg': 'Image',
    'png': 'Image',
    'jpg': 'Image',
    'jpeg': 'Image',
    'tif': 'Image',
    'raw': 'Image',
    'psd': 'Image',



}

fileformat('png', formatSet)
