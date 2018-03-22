#
"""
Generalized Heartbeat

Benjamin Tiernan

2018-03-21

Utility to provide a general monitor for checking the last 
runtime of various processes.

I'm converting some of the verbal arguments to positional arguments
to make the code a little more... approachable.

* CORRECTION: building a more robust scheme for the kwargs... 
principally, each function will have a secondary responsibility
to compare the kwargs passed against the default internal dict.

this is going to be a memory hog as a result, but should provide
a greater degree of usability.
"""

import time;
import sys;
import os;

# need to establish which path might have some of the other tools.
# need to establish what the packaging directory might look like...


# need to make the system a bit more efficient -
# aiming to reduce the footprint of the process with respect to 
# number of steps and number of endpoints.
#
# check_run() should basically have two conditions:
# 1) needs review
# 2) all clear.
#
# these cases can be represented by a simple true/false, which
# should then trigger other elements as needed.
# probably going to just start using this as my go to mechanism forkeyword based arguments.
#

def reconcile(dict_1, dict_2):
    """
    update dict_1 withe the contents of dict_2;
    """
    pass
    for a in dict_2.keys():
        dict_1.update({a:dict_2[a]});
    del dict_2;
    return dict_1;

# I'm allowing any keyword arguments to be passed in - I'm going to have
# 
# 1) get data.
# 2) update the dict
# 3) execute the function.
# mechanism works precisely as expected. I'm going to work on integrating/
# wrapping this mechanism with a larger application.
# correction this thing should be the application....
#
def check_run(**kwargs):
    """
    threshold argument should be in seconds.
    
    improved the mechanism with a 
    scheme providing support for standardized keyword arguments.
    not the cleanest solution, but also not the worst that I've 
    seen.
    
    if the "raise alert" flag is raised - simply return that there 
    was a service interruption - make sure that the elements are
    making more granular use of resources.
    
    Simplified the processing that this function is responsible for
    Logging will have to handle the specifics of the error in this
    model.
    """
    para = {
        'file':None,
        'alert':None,
        'threshold':None,
        'verbose':False
    }
    para = reconcile(para,kwargs);
    pass;
    # toggle this flag if there is a reason to return information.
    raise_alert = False;
    content = None;
    now = time.time();
    # on ANY error, raise the 'raise_alert' flag.
    # this will prevent localized service interruption, 
    # and will make sure the information has the 
    # apropriate resources allocated.
    try:
        with open(para['file']) as dt:
            content = dt.read();
        if now - float(content) > para['threshold']: raise_alert = True;
    except Exception as ECHO:
        sys.stdout.write(str(ECHO)+'\n')
        raise_alert = True;
    return raise_alert;
    
# might be useful to include this as part of a larger hearbeat program...
# if I'm going to use a separate mechanism, I should rename this one,
# and integrate "Reconcile" into my interpreter...
def recurring_beat():
    """
    """
    pass;
