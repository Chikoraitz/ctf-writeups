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

    self.__parser.add_argument("-p",
                                type = int,
                                required = True)
    self.__parser.add_argument("-q",
                                type = int,
                                required = True)

    self.__parser.add_argument("-e",
                                type = int,
                                help = "Chosen e : released as part of the public key",
                                required = True)

    self.__parser.add_argument("-c", "--cipher",
                                type = int,
                                help = "Ciphertext number",
                                required = True)

    self.__args = self.__parser.parse_args(cmd_args)


  def run(self)->None:
    """ Main body of the exploit """
    from Crypto.Util.number import inverse, long_to_bytes

    print(f"p : {self.__args.p}")
    print(f"q : {self.__args.q}")
    print(f"e : {self.__args.e}")
    print(f"c : {self.__args.cipher}")

    phi_n = (self.__args.p-1)*(self.__args.q-1)
    d = inverse(self.__args.e, phi_n)

    print(f"[+] phi(n) computed: {phi_n}")
    print(f"[+] Decryption key computed: {d}")
    print(f"[+] Decrypted message: {long_to_bytes(pow(self.__args.cipher,d,self.__args.p*self.__args.q))}")


def main(cmd_args: typing.List[str])->None:
  """ Get command line arguments

  : param cmd_args : List - List of arguments supplied

  Binds the command line arguments to the Exploit class constructor
  """
  script = Exploit(cmd_args)
  script.run()


if __name__ == "__main__":
  main(sys.argv[1:])
