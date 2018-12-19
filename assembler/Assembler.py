#!/usr/bin/env python
import MIPS

def assembleRFormat(assembly):
    opcode = MIPS.getOpCode(assembly[0])
    rs = MIPS.getRegCode(assembly[2])
    rt = MIPS.getRegCode(assembly[3])
    rd = MIPS.getRegCode(assembly[1])
    shamt = 0
    funct = MIPS.getFuncCode(assembly[0])
    machineCode = (opcode << 26) | (rs << 21) | (rt << 16) | (rd << 11) | (shamt << 6) | funct
    print(hex(machineCode))
    print(format(machineCode, '032b'))

def main():
    testInst = "add $t0,$s1,$s2"
    decomp = testInst.replace(',',' ').split()
    assembleRFormat(decomp)
#    print(MIPS.getOpCode(decomp[0]))
#    print(MIPS.getRegCode(decomp[2]))
#    print(MIPS.getRegCode(decomp[3]))
#    print(MIPS.getRegCode(decomp[1]))
#    print(MIPS.getFuncCode(decomp[0]))


if __name__ == "__main__":
    main()