/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_TRACKER_IQ_CHECKERPATTERN_H
#define INCLUDED_TRACKER_IQ_CHECKERPATTERN_H

#include <tracker/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace tracker {

    /*!
     * \brief <+description of block+>
     * \ingroup tracker
     *
     */
    class TRACKER_API iq_checkerpattern : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<iq_checkerpattern> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of tracker::iq_checkerpattern.
       *
       * To avoid accidental use of raw pointers, tracker::iq_checkerpattern's
       * constructor is in a private implementation
       * class. tracker::iq_checkerpattern::make is the public interface for
       * creating new instances.
       */
      static sptr make(float sample_rate, float frequency, float amplitude);
    };

  } // namespace tracker
} // namespace gr

#endif /* INCLUDED_TRACKER_IQ_CHECKERPATTERN_H */

