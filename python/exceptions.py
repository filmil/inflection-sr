""" List of exceptions that are easier to handle manually (for now). """

EXCEPTIONS = {
  'кћи': ['кћи', 'кћери', 'кћери', 'кћер', 'кћери', 'кћери', 'кћери', 'кћери', 'кћери', 'кћерима', 'кћери', 'кћери', 'кћерима', 'кћерима'],
  'мати': ['мати', 'матере', 'матери', 'матер', 'мати', 'матером', 'матери', 'матере', 'матера', 'матерама', 'матере', 'матере', 'матерама', 'матерама'],
}

def return_exception(singular):
  """ Returns full inflection list for a given noun, or None."""
  return EXCEPTIONS.get(singular)