#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import classification_report,auc,roc_auc_score
from PIL import Image
import time
from pathlib import Path

import os
import numpy as np
import pandas as pd
from PIL import Image

import warnings
warnings.filterwarnings('ignore', '.*do not.*', )
warnings.warn('Do not show this message')

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from glob import glob
#from skimage import io
from sklearn.utils import shuffle

#from nipype.interfaces.ants import N4BiasFieldCorrection
import sys

import warnings
warnings.filterwarnings('ignore')


def print_info(ims):

    for im in ims:
        
        print(im.shape, im.min(), im.max(), im.mean(), im.std(), \
              'n!=0:',im[im!=0].shape[0],im[im!=0].mean(),im.dtype)

def print_info_full(ims):

    for im in ims:
        
        print(im.shape, im.min(), im.max(), im.mean(), im.std(), \
              'n!=0:',im[im!=0].shape[0],'mean of!=0:',im[im!=0].mean(),im.dtype,
              'n uni:',len(np.unique(im.flatten())), 'quan 0.9:',
              np.quantile(im.flatten(), 0.9))


import os

def show_n_images_nsave(imgs, cmap='gray', titles=None, enlarge=4, mtitle=None,
                  cut=0, axis_off=True, fontsize=15, cb=0, imsave=0):
    plt.set_cmap(cmap)
    n = len(imgs)
    gs1 = gridspec.GridSpec(1, n)
    fig1 = plt.figure(figsize=(4*len(imgs), 8))
    
    for i in range(n):
        ax1 = fig1.add_subplot(gs1[i])
        if (cb):
            if len(np.unique(imgs[i])) <= 5:
                img = imgs[i]
            else:
                img = cont_br(imgs[i])
        else:
            img = imgs[i]
        if cut:
            ax1.imshow(img[50:290, 75:450], interpolation='none', origin='lower')
        else:
            ax1.imshow(img, interpolation='none')
        if (titles is not None):
            ax1.set_title(titles[i], fontsize=fontsize)
        if (axis_off):
            plt.axis('off')
    
    if mtitle:
        plt.suptitle(mtitle)
    
    plt.tight_layout()
    
    # Save images if requested
    if imsave:
        # Create directory if it doesn't exist
        save_dir = 'im_for_article'
        os.makedirs(save_dir, exist_ok=True)
        
        if titles is not None:
            # Save individual images
            for i in range(n):
                # Clean filename (remove special characters)
                filename = titles[i].replace(' ', '_').replace('/', '_').replace('\\', '_')
                filename = ''.join(c for c in filename if c.isalnum() or c in ['_', '-', '.'])
                filepath = os.path.join(save_dir, f"{filename}.png")
                
                # Create individual figure for each image
                fig_single = plt.figure(figsize=(6, 6))
                if (cb):
                    if len(np.unique(imgs[i])) <= 5:
                        img = imgs[i]
                    else:
                        img = cont_br(imgs[i])
                else:
                    img = imgs[i]
                
                if cut:
                    plt.imshow(img[50:290, 75:450], interpolation='none', origin='lower', cmap=cmap)
                else:
                    plt.imshow(img, interpolation='none', cmap=cmap)
                
                plt.title(titles[i], fontsize=fontsize)
                if axis_off:
                    plt.axis('off')
                
                plt.tight_layout()
                #plt.savefig(filepath, dpi=300, bbox_inches='tight')
                #plt.close(fig_single)
                #print(f"Saved: {filepath}")
        
        # Save the combined figure
        if mtitle:
            combined_filename = mtitle.replace(' ', '_').replace('/', '_').replace('\\', '_')
            combined_filename = ''.join(c for c in combined_filename if c.isalnum() or c in ['_', '-', '.'])
        else:
            combined_filename = 'combined_figure'+str(imsave)
        
        combined_filepath = os.path.join(save_dir, f"{combined_filename}_combined.png")
        fig1.savefig(combined_filepath, dpi=300, bbox_inches='tight')
        print(f"Saved combined figure: {combined_filepath}")
    
    plt.show()
    
def show_n_images(imgs, cmap='gray', titles = None, enlarge = 4, mtitle=None,
                  cut = 0, axis_off = True, fontsize=15, cb = 0,imsave=0):

    plt.set_cmap(cmap);

    n = len(imgs);
    gs1 = gridspec.GridSpec(1, n);

    fig1 = plt.figure(figsize=(4*len(imgs),8));
    for i in range(n):

        ax1 = fig1.add_subplot(gs1[i]);
        if (cb):
            if len(np.unique(imgs[i])<=5):
                 img = imgs[i]
            else:

                img = cont_br(imgs[i])
        else:
            img = imgs[i]
        if cut:
            ax1.imshow(img[50:290, 75:450] , interpolation='none', origin='lower');
        else:

            ax1.imshow(img, interpolation='none');
        if (titles is not None):
            ax1.set_title(titles[i], fontsize=fontsize); 
        if (axis_off):
            plt.axis('off')
    if mtitle:
        plt.title(mtitle)
    plt.tight_layout()
    plt.show();

#------------------------------------------------------------------------------