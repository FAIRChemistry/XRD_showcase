# Example for XRD data 

This is just a tiny example to show how a notebook for XRD can look like when provided with some data.


### Dataset

...

- __name_exp__
  - Type: string
  - Description: Name of the experimentator.
- __date__
  - Type: date
  - Description: Date when the sample was measured.
- __compound__
  - Type: string
  - Description: Name of the compound.
- __sample_id__
  - Type: string
  - Description: ID of the measured sample
- __spec_inf__
  - Type: SpecInf
  - Description: Information about the spectrometer.


### SpecInf

Information about the spectrometer.

- __wl__
  - Type: Wavelength
  - Description: different wavelengths of the X-ray.
  - Multiple: True
- __wl_ratio__
  - Type: float
  - Description: ...
- __anode__
  - Type: string
  - Description: Material of the anode.
- __steptime__
  - Type: float
  - Description: Steptime in ...
- __stepsize__
  - Type: float
  - Description: Stepsize in degree.
- __start__
  - Type: float
  - Description: Starting angle in degrees.
- __theta__
  - Type: float
  - Description: Theta.
- __theta2__
  - Type: float
  - Description: TwoTheta.


### Wavelength

...

  - Type: float
  - Description: Wavelength in Angstrom.