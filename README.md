gaexperiment
============

A small python library to use with your google experiment setup. In order to
use it, you have to do the following:

- Create an instance of GaExperiment. It accepts the experiment's code/id,
  a whitelist array specifying the variations and a dictionary with the get
  variables from the request (the code is framework agnostic, so you can
  inject your frameworks implementation there).
- Rendering the template, make the above instance available as a variable and
  it can generate the js code for the experiment for you. If for example the
  instance is passed as gaexp in the template, by using gaexp.code, you get
  the experiment code to be used. It is displayed only on the original page,
  as this code is not needed in variation templates.
- Also, the library has a helper method template_to_serve that returns the 
  template file name based on a base name you pass to it.
  For example: gaexp.template_to_serve('landing.pt') will return either
  'landing.pt' or 'landing_v2.pt' if the variation of the experiment has a get
  variable 'gaexp=v2'. This is the convention used here.

In general the library expects the variations of the experiment to have the
same URL and differentiate in a get variable named 'gaexp'. So, when creating
your experiments, the variations should have urls like: original_url?gaexp=v1
and so on.
