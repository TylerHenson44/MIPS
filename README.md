# MIPS
MIPS Processor in VHDL &amp; Assembler 

## Components

### Assembler
Python scripts to turn MIPS Assembly into machine code. Will update with supported commands as added.

Notes:
- Totally a work in progress, not anywhere close to what the final product will look like
- Current attempt at implementation is not object oriented and will be more script like.
- Want to make improvements to have instructions as objects
- Would provide the assembly instruction to an object factory that would return an object of the correct type
- The 3 types would be:
    - R Format
    - I Format
    - J Format

### Processor
VHDL representation of a MIPS processor. I plan to have subdirectories with component libraries I have created and then the final put together processor.
Will begin with a single clock cycle per instruction and move on to pipelined. May change repo structure later.
