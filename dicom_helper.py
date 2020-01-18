import numpy as np 
import matplotlib.pyplot as plt 
import pydicom as dicom 

a_dcm_file = "./data_kaggle/train/1/study/sax_5/IM-4557-0001.dcm"

raw_file = dicom.read_file(a_dcm_file)

print(raw_file)