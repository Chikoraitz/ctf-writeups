#!/usr/bin/python3

import argparse
import typing
import sys


class Exploit:
  """ Exploit class """

  def __init__(self, cmd_args: typing.List[str])->None:
    """ Argument checker
    : param cmd_args : List - List of arguments supplied

    Validate the arguments.
    Throws an exception if the validation fails.
    """
    self.__parser = argparse.ArgumentParser(
      description = "PicoCTF - Mind your Ps and Qs"
    )

    self.__parser.add_argument("-n",
                                type = 
                                help = "",
                                required = True)
    self.__parser.add_argument("-e",
                                type = 
                                help = "",
                                required = True)
    self.__parser.add_argument("-c", "--cipher",
                                type = 
                                help = "",
                                required = True)

    self.__args = self.__parser.parse_args(cmd_args)


  def run(self)->None:
    """ Main body of the exploit """


def main(cmd_args: typing.List[str])->None:
  """ Get command line arguments

  : param cmd_args : List - List of arguments supplied

  Binds the command line arguments to the Exploit class constructor
  """
  script = Exploit(cmd_args)
  script.run()


if __name__ == "__main__":
  main(sys.argv[1:])
