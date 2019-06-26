########################################################################
class Basic:
    """
    Contains the basic parameters to train the Motor Imagery algorithm
    """

    #-------------------------------------------
    # Data 
    #-------------------------------------------
    params1 = dict()
    params1.update({'DATA_PATH': str})                               # read all data files from this directory to train on
    
    #-------------------------------------------
    # Events
    #-------------------------------------------
    params2 = dict()
    # Issue: Think about it, maybe split in 2
    params2.update({'EPOCH': list})

    # example
    #params2.update({'EPOCH1':{'range':[0, 3]}})
    #params2.update({'EPOCH2':{'range':[0, 3]}})
 
    #-------------------------------------------
    # Channels specification
    #-------------------------------------------
    params3 = dict()
    params3.update({'PICKED_CHANNELS': list})                               # Pick a subset of channels for PSD.
    params3.update({'EXCLUDED_CHANNELS': list})                             # Overwrite the CHANNEL_PICKS
    params3.update({'REF_CHANNELS_OLD': list})                            # Recover this channel which was used as reference channel.
    params3.update({'REF_CHANNELS_NEW': list})                            # Re-reference to this set of channels, averaged if more than 1.

    #-------------------------------------------
    # Filters
    #-------------------------------------------
    params5 = dict()
    params5.update({'SP_FILTER': (None, 'car', 'laplacian')})      # apply spatial filter immediately after loading data
    params5.update({'SP_CHANNELS': list})                             # only consider the following channels while computing
    # apply spectrial filter immediately after applying SP_FILTER
    # Can be either overlap-add FIR or forward-backward IIR via filtfilt
        # if lfreq < hfreq: bandpass
        # if lfreq > hfreq: bandstop
        # if lfreq == None: highpass
        # if hfreq == None: lowpass
    params5.update({'TP_FILTER': list})                            # None or [lfreq, hfreq]
    params5.update({'NOTCH_FILTER': list})                         # None or list of values

    # example
    #params5.update({'TP_FILTER': {'None':[None, None], 'lowpass',[None, 30], 'bandpass':[1, 40], 'highpass':[8, None]}})


    #-------------------------------------------
    # Parallel processing
    #-------------------------------------------
    params6 = dict()
    params6.update({'N_JOBS': int})                               # number of cores used for parallel processing (set None to use all cores)


########################################################################
class Advanced:
    """
    Contains the advanced parameters to train the Motor Imagery algorithm`
    """

    #-------------------------------------------
    # Trigger
    #-------------------------------------------
    params1 = dict()                            
    params1.update({'TRIGGER_FILE': str})                            # which trigger file template
    params1.update({'TRIGGER_DEF': str})                             # which trigger set?
    
   
    #-------------------------------------------
    # Unit conversion
    #-------------------------------------------
    params2 = dict()
    params2.update({'MULTIPLIER': int})

    #-------------------------------------------
    # Feature types
    #-------------------------------------------
    params3 = dict()
    params3.update({'FEATURES': ('PSD')})
    params3.update({'EXPORT_GOOD_FEATURES': (False, True)})
    params3.update({'FEAT_TOPN': int})                             # show only the top N features

    #-------------------------------------------
    # PSD 
    #-------------------------------------------
    # wlen: window length in seconds
    # wstep: window step in absolute samples (32 is enough for 512 Hz, or 256 for 2KHz)
    params5 = dict()
    params5.update({'PSD': dict(fmin=int, fmax=int, wlen=float, wstep=int)})

    #-------------------------------------------
    # Classifier
    #-------------------------------------------
    #{'CLASSIFIER': {'GB':dict(trees=1000, learning_rate=0.01, max_depth=3, seed=666)}, 'RF':dict()}}

    params6 = dict()
    params6.update({'CLASSIFIER': ('GB', 'XGB', 'RF', 'rLDA', 'LDA')})
    params6.update({'GB': dict(trees=int, learning_rate=float, max_depth=int, seed=int)})
    params6.update({'RF': dict(trees=int, max_depth=int, seed=int)})
    params6.update({'EXPORT_CLS': (False, True)})
    params6.update({'RLDA_REGULARIZE_COEFF': float})

    #-------------------------------------------
    # Cross-Validation & testing
    #-------------------------------------------
    params7 = dict()
    params7.update({'CV_PERFORM': (None, 'StratifiedShuffleSplit', 'LeaveOneOut')})
    params7.update({'CV_TEST_RATIO': float})                         # StratifiedShuffleSplit only
    params7.update({'CV_FOLDS': int })                             # StratifiedShuffleSplit only
    params7.update({'CV_RANDOM_SEED': int})                        # StratifiedShuffleSplit only
    params7.update({'CV_EXPORT_RESULT': (False, True)})             # Common