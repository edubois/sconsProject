from _external import *

tiff = LibWithHeaderChecker('tiff','tiff.h','c',call='TIFFGetVersion();')
