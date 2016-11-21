#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Nov 18 12:20:56 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import tracker
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_0 = variable_0 = 0
        self.samp_rate = samp_rate = 8e6
        self.ppm_corr = ppm_corr = 0
        self.low_cutoff = low_cutoff = 1e3
        self.high_cutoff = high_cutoff = 100e3
        self.ffactor = ffactor = 1e0
        self.Frequency_0 = Frequency_0 = 433000000
        self.Frequency = Frequency = 433e6

        ##################################################
        # Blocks
        ##################################################
        _ppm_corr_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ppm_corr_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ppm_corr_sizer,
        	value=self.ppm_corr,
        	callback=self.set_ppm_corr,
        	label='ppm_corr',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ppm_corr_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ppm_corr_sizer,
        	value=self.ppm_corr,
        	callback=self.set_ppm_corr,
        	minimum=-5e2,
        	maximum=5e2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_ppm_corr_sizer)
        self.wxgui_scopesink2_0_0_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0_0_0.win)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0_0.win)
        self.tracker_iq_checkerpattern_0 = tracker.iq_checkerpattern(10.0, 10.0, 0.7)
        self.osmosdr_source_0_0 = osmosdr.source( args="numchan=" + str(1) + " " + "bladerf=9bd" )
        self.osmosdr_source_0_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.osmosdr_source_0_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0_0.set_center_freq(Frequency, 0)
        self.osmosdr_source_0_0.set_freq_corr(0, 0)
        self.osmosdr_source_0_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0_0.set_gain_mode(False, 0)
        self.osmosdr_source_0_0.set_gain(0, 0)
        self.osmosdr_source_0_0.set_if_gain(20, 0)
        self.osmosdr_source_0_0.set_bb_gain(20, 0)
        self.osmosdr_source_0_0.set_antenna("", 0)
        self.osmosdr_source_0_0.set_bandwidth(0, 0)
          
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "bladerf=24d" )
        self.osmosdr_source_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(Frequency + ppm_corr * 10, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(20, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "bladerf=9bd" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(Frequency, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(20, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        _low_cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._low_cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_low_cutoff_sizer,
        	value=self.low_cutoff,
        	callback=self.set_low_cutoff,
        	label='low_cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._low_cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_low_cutoff_sizer,
        	value=self.low_cutoff,
        	callback=self.set_low_cutoff,
        	minimum=0,
        	maximum=1500e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_low_cutoff_sizer)
        _high_cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._high_cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_high_cutoff_sizer,
        	value=self.high_cutoff,
        	callback=self.set_high_cutoff,
        	label='high_cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._high_cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_high_cutoff_sizer,
        	value=self.high_cutoff,
        	callback=self.set_high_cutoff,
        	minimum=0,
        	maximum=1500e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_high_cutoff_sizer)
        _ffactor_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ffactor_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ffactor_sizer,
        	value=self.ffactor,
        	callback=self.set_ffactor,
        	label='ffactor',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ffactor_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ffactor_sizer,
        	value=self.ffactor,
        	callback=self.set_ffactor,
        	minimum=0,
        	maximum=15,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_ffactor_sizer)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 0, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.tracker_iq_checkerpattern_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_scopesink2_0_0, 0))    
        self.connect((self.osmosdr_source_0_0, 0), (self.wxgui_scopesink2_0_0_0, 0))    
        self.connect((self.tracker_iq_checkerpattern_0, 0), (self.osmosdr_sink_0, 0))    

    def get_variable_0(self):
        return self.variable_0

    def set_variable_0(self, variable_0):
        self.variable_0 = variable_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0_0.set_sample_rate(self.samp_rate)

    def get_ppm_corr(self):
        return self.ppm_corr

    def set_ppm_corr(self, ppm_corr):
        self.ppm_corr = ppm_corr
        self._ppm_corr_slider.set_value(self.ppm_corr)
        self._ppm_corr_text_box.set_value(self.ppm_corr)
        self.osmosdr_source_0.set_center_freq(self.Frequency + self.ppm_corr * 10, 0)

    def get_low_cutoff(self):
        return self.low_cutoff

    def set_low_cutoff(self, low_cutoff):
        self.low_cutoff = low_cutoff
        self._low_cutoff_slider.set_value(self.low_cutoff)
        self._low_cutoff_text_box.set_value(self.low_cutoff)

    def get_high_cutoff(self):
        return self.high_cutoff

    def set_high_cutoff(self, high_cutoff):
        self.high_cutoff = high_cutoff
        self._high_cutoff_slider.set_value(self.high_cutoff)
        self._high_cutoff_text_box.set_value(self.high_cutoff)

    def get_ffactor(self):
        return self.ffactor

    def set_ffactor(self, ffactor):
        self.ffactor = ffactor
        self._ffactor_slider.set_value(self.ffactor)
        self._ffactor_text_box.set_value(self.ffactor)

    def get_Frequency_0(self):
        return self.Frequency_0

    def set_Frequency_0(self, Frequency_0):
        self.Frequency_0 = Frequency_0

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        self.osmosdr_sink_0.set_center_freq(self.Frequency, 0)
        self.osmosdr_source_0.set_center_freq(self.Frequency + self.ppm_corr * 10, 0)
        self.osmosdr_source_0_0.set_center_freq(self.Frequency, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
