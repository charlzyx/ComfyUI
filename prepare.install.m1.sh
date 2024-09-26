#!/bin/bash

# 1. install conda
# https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links
conda create -n comfyenv
conda activate comfyenv

conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly

