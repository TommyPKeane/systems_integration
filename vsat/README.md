# Very Small Aperature Antenna (VSAT) Systems

VSAT System-Integration is essentially the coordination of modular electronic devices for RF/IF mixing, Modulation-Demodulation of signals, and  transmission/reception of energy.

VSATs are essentially antenna-dishes and components that are "Portable Earth-Stations" for facillitating a satellite link.

The code and documentation, here, addresses the nuanced technical aspects of Signal Processing and Spectral Characteristics for integrating the components that go into typical VSAT Systems.

I've never had any kind of government clearance, and I no longer work for a VSAT integrator or manufacturer, so everything provided here is of my own designs, based in publically available datasheets, and is meant for educational/conversational purposes only.

# sigproc Package

Provides __Signal Processing__ devices and utility-functions to support integrations and communications between VSAT devices.

## Mixer(s)

The `UpMixer` and `DnMixer` classes provide the base-classes for LNBs (`DnMixer`) and BUCs (`UpMixer`), in the abstract sense of them being frequency mixers.

These are designed to default to `decimal.Decimal` instances for frequency values instead of `float` instances.

`decimal.Decimal` objects support `128`-bit floating-point precision through [Decimal Floating-Point](https://en.wikipedia.org/wiki/Decimal_floating_point) (DFP) implementations.

This is _not_ to be confused with [Fixed-Point](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) numbers -- which are much more restricted in the supported range of values.

> __Note:__ The values used in the Unit-Tests for Mixer classes, by default, are assumed to be `[GHz]`-range values. Representing `10 [kHz]` would be `0.000_010 [GHz]`. The Mixer classes themselves have no current notion of units, so they will support any units-scale, as long as you are consistent within and between classes (unless you implement your own external converters).

> `@TODO`: The `energy` module will be implemented to support self-transformable frequencies.

# modem Package

_Stay tuned... (modem devices)_

# buc Package

_Stay tuned... (BUC/PA devices)_

# lnb Package

_Stay tuned... (LNB/LNA devices)_

# tests Package

Unit-Tests for the other packages.

These tests rely only on the Python Standard Library (PSL), so you can run them by simply calling:

```bash
python ./run_tests.py
```

From the same directory as this README (call `cd vsat` after cloning this repository to a local directory).

# Copyright and License

Copyright, 2020, Tommy P. Keane

See top-level `LICENSE` file in this repository.

If you want to use this `vsat` project separately, please be sure to carry-over the `LICENSE` file and source-attribution. Thanks!