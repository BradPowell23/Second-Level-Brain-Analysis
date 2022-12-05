import sys
sys.path.insert(0, 'src')

import nilearn
import numpy as np
import pandas as pd
from nilearn import plotting
from nilearn import image
from nilearn.glm.first_level import make_first_level_design_matrix
from nilearn.plotting import plot_stat_map, plot_anat, plot_img, view_img
from nilearn.glm.first_level import FirstLevelModel
from nilearn.image import concat_imgs, mean_img
from nilearn.plotting import plot_contrast_matrix
import matplotlib.pyplot as plt
from nilearn.glm import threshold_stats_img
from numpy import array
from nilearn.image import concat_imgs, index_img

from src import single_run

def main(targets):
    '''
    Runs target test on the test data
    '''
    if 'test' in targets:
        single_run('test/testdata/test_1.nii.gz')
    return

if __name__ == '__main__':
    targets = sys.argv[2:]
    main(targets)
