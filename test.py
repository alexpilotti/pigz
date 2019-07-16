import ctypes
from ctypes import cdll
import sys
l = cdll.LoadLibrary('pigz.so')
l.main.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)]
l.main.retval = ctypes.c_int

args = ["pigz", "-0", "-f", "-k", "README"]
argc = len(args)
argv = (ctypes.c_char_p * (argc + 1))()

for i, arg in enumerate(args):
    enc_arg = arg.encode('utf-8')
    argv[i] = ctypes.c_char_p(enc_arg)

l.main(argc, argv)
