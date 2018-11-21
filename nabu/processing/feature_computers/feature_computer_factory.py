'''@file feature_computer_factory.py
contains the FeatureComputer factory'''

import mfcc
import fbank
import logspec
import magspec
import spec
import raw

def factory(feature):
    '''
    create a FeatureComputer

    Args:
        feature: the feature computer type
    '''

    if feature == 'fbank':
        return fbank.Fbank
    elif feature == 'mfcc':
        return mfcc.Mfcc
    elif feature == 'logspec':
        return logspec.Logspec
    elif feature == 'magspec':
        return magspec.Magspec
    elif feature == 'spec':
        return spec.Spec
    elif feature == 'raw':
        return raw.Raw
    else:
        raise Exception('Undefined feature type: %s' % feature)
