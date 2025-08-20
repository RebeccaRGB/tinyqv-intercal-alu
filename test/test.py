# SPDX-FileCopyrightText: © 2025 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

from tqv import TinyQV

# When submitting your design, change this to the peripheral number
# in peripherals.v.  e.g. if your design is i_user_peri05, set this to 5.
# The peripheral number is not used by the test harness.
PERIPHERAL_NUM = 36

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 100 ns (10 MHz)
    clock = Clock(dut.clk, 100, units="ns")
    cocotb.start_soon(clock.start())

    # Interact with your design's registers through this TinyQV class.
    # This will allow the same test to be run when your design is integrated
    # with TinyQV - the implementation of this class will be replaces with a
    # different version that uses Risc-V instructions instead of the SPI test
    # harness interface to read and write the registers.
    tqv = TinyQV(dut, PERIPHERAL_NUM)

    # Reset
    await tqv.reset()

    dut._log.info("Test project behavior")

    # Test register write and read back
    await tqv.write_word_reg(0, 0x82345678)
    await tqv.write_word_reg(4, 0x89ABCDEF)
    assert await tqv.read_hword_reg(0) == 0x5678
    assert await tqv.read_hword_reg(2) == 0x8234
    assert await tqv.read_hword_reg(4) == 0xCDEF
    assert await tqv.read_hword_reg(6) == 0x89AB
    assert await tqv.read_word_reg(0) == 0x82345678
    assert await tqv.read_word_reg(4) == 0x89ABCDEF

    # Write to low 16 bits
    await tqv.write_hword_reg(0, 0x7777)
    await tqv.write_hword_reg(4, 0x5656)
    assert await tqv.read_hword_reg(0) == 0x7777
    assert await tqv.read_hword_reg(2) == 0x8234
    assert await tqv.read_hword_reg(4) == 0x5656
    assert await tqv.read_hword_reg(6) == 0x89AB
    assert await tqv.read_word_reg(0) == 0x82347777
    assert await tqv.read_word_reg(4) == 0x89AB5656

    # Write to high 16 bits
    await tqv.write_hword_reg(2, 0xBABA)
    await tqv.write_hword_reg(6, 0xDADA)
    assert await tqv.read_hword_reg(0) == 0x7777
    assert await tqv.read_hword_reg(2) == 0xBABA
    assert await tqv.read_hword_reg(4) == 0x5656
    assert await tqv.read_hword_reg(6) == 0xDADA
    assert await tqv.read_word_reg(0) == 0xBABA7777
    assert await tqv.read_word_reg(4) == 0xDADA5656

    # TODO
