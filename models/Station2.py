import ipaddress
from masoniteorm.models import Model

class Station2(Model):
  """Station Model"""
  __table__ = "stations"

  __appends__ = [ "ip_address" ]

  # Gets ip as a ipaddress class

  def get_ip_address_attribute(self):
    return ipaddress.ip_address(self.ip)

  # Save ip on database as an integer
  def set_ip_attribute(self, attribute):
    return int(ipaddress.ip_address(attribute))