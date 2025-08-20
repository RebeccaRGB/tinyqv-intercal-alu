<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

The peripheral index is the number TinyQV will use to select your peripheral.  You will pick a free
slot when raising the pull request against the main TinyQV repository, and can fill this in then.  You
also need to set this value as the PERIPHERAL_NUM in your test script.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

# INTERCAL ALU

Author: Rebecca G. Bettencourt

Peripheral index: 36

## What it does

(TODO)

## Register map

| Address | Name  | Access | Description                                                         |
|---------|-------|--------|---------------------------------------------------------------------|
| 0x00    | A     | R/W 32 | Left side argument, 32 bits.                                        |
| 0x00    | AL    | R/W 16 | Left side argument, low 16 bits.                                    |
| 0x02    | AH    | R/W 16 | Left side argument, high 16 bits.                                   |
| 0x04    | B     | R/W 32 | Right side argument, 32 bits.                                       |
| 0x04    | BL    | R/W 16 | Right side argument, low 16 bits.                                   |
| 0x06    | BH    | R/W 16 | Right side argument, high 16 bits.                                  |

(TODO)
