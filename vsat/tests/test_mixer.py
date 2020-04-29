#!/usr/bin/python
#
# Tommy P. Keane
# talk@tommypkeane.com

import decimal;
import logging;
import unittest;

from sigproc import mixer;

class BaseMixerTest(unittest.TestCase):
   """Test Class for mixer.Mixer class."""

   @classmethod
   def setUpClass(cls):
      """Pre-Initialize local namespace to support test methods."""
      return None;
   # fed

   def test_mix(self,):
      step_count = 20;
      freq_step = (
         (self.input_range[1] - self.input_range[0])
         / step_count
      );
      for x in range(0, step_count, 1):
         f = self.input_range[0] + (freq_step * x);
         with self.subTest(f= f):
            mixed_f = self.mixer_obj.mix(f);
            self.assertGreaterEqual(mixed_f, self.output_range[0]);
            self.assertLessEqual(mixed_f, self.output_range[1]);
         # htiw
      # rof
      return None;
   # fed

   @classmethod
   def tearDownClass(cls):
      """Cleanup any pre-initialization objects and logging after tests run."""
      return None;
   # fed
# ssalc


class HiDnMixerTest(BaseMixerTest):
   """Test Class for mixer.Mixer class."""

   @classmethod
   def setUpClass(cls):
      """Pre-Initialize local namespace to support test methods."""
      return None;
   # fed

   def setUp(self,):
      self.brand = "Norsat";
      self.model = "8515";
      self.noise_figure = decimal.Decimal(0.700);  # dB
      self.lo_stability = decimal.Decimal(0.000_500_0);  # GHz
      self.lo_freq = decimal.Decimal(5.150);  # GHz
      self.input_range = [decimal.Decimal(3.400), decimal.Decimal(4.200_000_001),];  # GHz
      self.output_range = [decimal.Decimal(0.950), decimal.Decimal(1.750_000_001),];  # GHz
      self.mixer_obj = mixer.DnMixer(
         self.lo_freq,
         self.input_range,
      );
      return None;
   # fed

   def tearDown(self,):
      return None;
   # fed

   @classmethod
   def tearDownClass(cls):
      """Cleanup any pre-initialization objects and logging after tests run."""
      return None;
   # fed
# ssalc


class LoDnMixerTest(BaseMixerTest):
   """Test Class for mixer.Mixer class."""

   @classmethod
   def setUpClass(cls):
      """Pre-Initialize local namespace to support test methods."""
      return None;
   # fed

   def setUp(self,):
      self.brand = "Norsat";
      self.model = "X1000HA";
      self.noise_figure = decimal.Decimal(0.700);  # dB
      self.lo_stability = decimal.Decimal(0.000_012_5);  # GHz
      self.lo_freq = decimal.Decimal(6.300);  # GHz
      self.input_range = [decimal.Decimal(7.250), decimal.Decimal(7.750_000_001),];  # GHz
      self.output_range = [decimal.Decimal(0.950), decimal.Decimal(1.450_000_001),];  # GHz
      self.mixer_obj = mixer.DnMixer(
         self.lo_freq,
         self.input_range,
      );
      return None;
   # fed

   def tearDown(self,):
      return None;
   # fed

   @classmethod
   def tearDownClass(cls):
      """Cleanup any pre-initialization objects and logging after tests run."""
      return None;
   # fed
# ssalc

def load_tests(loader, tests, pattern):
   """Create a runnable test-suite instance.

   This is a specially named method for the PSL `unittest` module that
   determines which test-methods per Class are discoverable.
   """
   testsuite_obj = unittest.TestSuite()

   loside_tests = loader.loadTestsFromTestCase(LoDnMixerTest);
   hiside_tests = loader.loadTestsFromTestCase(HiDnMixerTest);

   testsuite_obj.addTests(loside_tests);
   testsuite_obj.addTests(hiside_tests);

   return testsuite_obj;
# fed
