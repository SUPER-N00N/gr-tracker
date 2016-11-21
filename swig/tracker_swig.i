/* -*- c++ -*- */

#define TRACKER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "tracker_swig_doc.i"

%{
#include "tracker/iq_checkerpattern.h"
%}


%include "tracker/iq_checkerpattern.h"
GR_SWIG_BLOCK_MAGIC2(tracker, iq_checkerpattern);
