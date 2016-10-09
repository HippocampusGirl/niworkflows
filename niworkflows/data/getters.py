#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
#
# @Author: oesteban
# @Date:   2016-01-05 11:29:40
# @Email:  code@oscaresteban.es
# @Last modified by:   oesteban
# @Last Modified time: 2016-09-23 11:52:11
"""
Data grabbers
"""
from __future__ import print_function, division, absolute_import, unicode_literals

from niworkflows.data.utils import _get_dataset_dir, _fetch_file

OSF_PROJECT_URL = ('https://files.osf.io/v1/resources/fvuh8/providers/osfstorage/')
OSF_RESOURCES = {
    'brainweb': ('57f32b96b83f6901f194c3ca', '384263fbeadc8e2cca92ced98f224c4b'),
    'ds003_downsampled': ('57f328f6b83f6901ef94cf70', '5a558961c1eb5e5f162696d8afa956e8'),
    'mni_template': ('57f32ab29ad5a101fb77fd89', 'debfa882b8c301cd6d75dd769e73f727'),
    'mni_template_RAS': ('57f32a799ad5a101f977eb77', 'a4669f0e7acceae148bb39450b2b21b4'),
    'ants_oasis_template': ('57f32ae89ad5a101f977eb79', '34d39070b541c416333cc8b6c2fe993c'),
    'ants_oasis_template_ras': ('57f32af06c613b01ed13d5fb', '74b2f126d59ddc8a55d76cd5af4774f7'),
    'mni_epi': ('57fa09cdb83f6901d93623a0', '9df727e1f742ec55213480434b4c4811'),
}

def get_dataset(dataset_name, data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the BIDS-fied brainweb 1mm normal


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    file_id, md5 = OSF_RESOURCES[dataset_name]
    if url is None:
        url = '{}/{}'.format(OSF_PROJECT_URL, file_id)

    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir, verbose=verbose)

    if _fetch_file(url, data_dir, filetype='tar', resume=resume, verbose=verbose,
                   md5sum=md5):
        return data_dir
    else:
        return None

def get_brainweb_1mm_normal(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the BIDS-fied brainweb 1mm normal


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    return get_dataset('brainweb', data_dir, url, resume, verbose)

def get_ds003_downsampled(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the BIDS-fied ds003_downsampled


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    return get_dataset('ds003_downsampled', data_dir, url, resume, verbose)

def get_mni_template(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    return get_dataset('mni_template', data_dir, url, resume, verbose)

def get_mni_template_ras(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('mni_template_RAS', data_dir, url, resume, verbose)

def get_mni_epi(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('mni_epi', data_dir, url, resume, verbose)

def get_ants_oasis_template(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the ANTs template of the OASIS dataset.
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('ants_oasis_template', data_dir, url, resume, verbose)

def get_ants_oasis_template_ras(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the ANTs template of the OASIS dataset.
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('ants_oasis_template_ras', data_dir, url, resume, verbose)