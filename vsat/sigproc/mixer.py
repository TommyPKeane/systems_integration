#!/usr/bin/python
#
# Tommy P. Keane
# talk@tommypkeane.com

import decimal;
import enum;
import typing;

from . import energy;


class MIXER_KINDS(enum.Enum):
   UP = "Up-Mixer";
   DN = "Down-Mixer";
# ssalc


class MIXER_SIDE(enum.Enum):
   HI = decimal.Decimal(1);
   LO = decimal.Decimal(-1);
# ssalc


class Mixer(object):
   """(Base) Generic Up/Down Mixer Class

   A class for defining modular up-/down-mixer devices as objects.
   """
   freq_range = typing.Optional[MIXER_KINDS];
   freq_lo = typing.Optional[decimal.Decimal];
   mixer_kind = typing.Optional[MIXER_KINDS];
   mix_sgn = typing.Optional[decimal.Decimal];

   def __init__(
      self,
      lo_freq,
      input_range,
   ):
      self.freq_in_min = decimal.Decimal(input_range[0]);
      self.freq_in_max = decimal.Decimal(input_range[1]);
      self.freq_lo = decimal.Decimal(lo_freq);
      if (self.freq_lo > self.freq_in_max):
         self.mix_sgn = MIXER_SIDE.HI;
      else:
         self.mix_sgn = MIXER_SIDE.LO;
      # fi
      return None;
   #fed
#ssalc


class DnMixer(Mixer):
   """Base Class for Frequency Down-Mixer Devices."""

   mixer_kind = MIXER_KINDS.DN;

   def mix(self, new_freq):
      mixed_freq = self.mix_sgn.value * (self.freq_lo - decimal.Decimal(new_freq));
      return (mixed_freq);
   #fed
# ssalc


class UpMixer(Mixer):
   """Base Class for Frequency Up-Mixer Devices."""

   mixer_kind = MIXER_KINDS.UP;

   def mix(self, new_freq):
      mixed_freq = self.freq_lo + (self.mix_sgn.value * decimal.Decimal(new_freq));
      return (mixed_freq);
   #fed
# ssalc
