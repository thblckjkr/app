import ipaddress
from masoniteorm.models import Model

class Station(Model):
  """Station Model"""

  # Gets ip as a ipaddress class
  def get_ip_attribute(self):
    return ipaddress.ip_address(self.ip)

  # Save ip on database as an integer
  def set_ip_attribute(self, attribute):
    return int(ipaddress.ip_address(attribute))