"""
AGP - calculate agp values given some glucose text
"""

##########################################
#
# openaps vendor example:
# The following shows what is needed to make the module available as a vendor
# plugin to openaps.
#

# Inherit from openaps.uses.use.Use class
from openaps.uses.use import Use

from agp import AGP
class calculate (Use):
  """ Calculate agp
  """

  # get_params helps openaps save your configurations
  def get_params (self, args):
    """
    Create a dict data type from args namespace so that config serializer can
    save these args for report generation.
    """
    return dict(input=args.input)

  # configure_app allows your plugin to specify command line parameters
  def configure_app (self, app, parser):
    """
    Set up any arguments needed by this use.
    """
    # get file based argument called input.
    parser.add_argument('input', default='glucose.txt')

  def prerender_text (self, data):
    out = [ ]
    for hour, minute, vals in data:
      out.append(' '.join(map(str, [hour, minute, ','.join(map(str, vals))])))
      # print hour, minute, vals
    return "\n".join(out)

  # main logic for the app
  def main (self, args, app):
    """
    Main logic for calculating agp
    """
    # print args
    # get parameters
    params = self.get_params(args)
    # print params.get('input')
    # create calculator
    parser = AGP( )
    with open(params.get('input'), 'r') as f:
      # calculate agp for all input
      return parser(f.readlines())

# set_config is needed by openaps for all vendors.
# set_config is used by `device add` commands so save any needed
# information.
# See the medtronic builtin module for an example of how to use this
# to save needed information to establish sessions (serial numbers,
# etc).
def set_config (args, device):
  # no special config
  return

# display_device allows our custom vendor implementation to include
# special information when displaying information about a device using
# our plugin as a vendor.
def display_device (device):
  # no special information needed to run
  return ''

# openaps calls get_uses to figure out how how to use a device using
# agp as a vendor.  Return a list of classes which inherit from Use,
# or are compatible with it:
def get_uses (device, config):
  # make agp an openaps use command
  return [ calculate ]

######################################################
# openaps definitions are complete
######################################################

