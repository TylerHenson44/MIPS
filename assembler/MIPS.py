#!/usr/bin/env python

opCodes = {
    'add' : 0b000000,
    'sub' : 0b000000,
    'addi': 0b001000,
    'lw'  : 0b100011,
    'sw'  : 0b101011
}

funcCodes = {
    'add' : 0b100000,
    'sub' : 0b100010
}

regCodes = {
    '$t0' : 0b01000,
    '$t1' : 0b01001,
    '$t2' : 0b01010,
    '$t3' : 0b01011,
    '$t4' : 0b01100,
    '$t5' : 0b01101,
    '$t6' : 0b01110,
    '$t7' : 0b01111,
    '$s0' : 0b10000,
    '$s1' : 0b10001,
    '$s2' : 0b10010,
    '$s3' : 0b10011,
    '$s4' : 0b10100,
    '$s5' : 0b10101,
    '$s6' : 0b10110,
    '$s7' : 0b10111,
}

rInstructions = [
    "add",
    "addu",
    "and",
    "jr",
    "nor",
    "or",
    "slt",
    "sltu",
    "sll",
    "srl",
    "sub",
    "subu"
]

def getOpCode(inst):
    return opCodes[inst]

def getRegCode(reg):
    return regCodes[reg]

def getFuncCode(func):
    return funcCodes[func]

def isRFormat(inst):
    return inst in rInstructions