rule MalElf {
    meta:
        description = "Malicious ELF binary"

    strings:
        $x1 = {e3 82 89 e3 81 9b e3 82 93 e9 9a 8e e6 ae b5}
        $x2 = {e3 82 ab e3 83 96 e3 83 88 e8 99 ab}
        $x3 = {e5 bb 83 e5 a2 9f e3 81 ae e8 a1 97}
        $x4 = {e3 82 a4 e3 83 81 e3 82 b8 e3 82 af e3 81 ae e3 82 bf e3 83 ab e3 83 88}
        $x5 = {e3 83 89 e3 83 ad e3 83 ad e3 83 bc e3 82 b5 e3 81 b8 e3 81 ae e9 81 93}
        $x6 = {e7 89 b9 e7 95 b0 e7 82 b9}
        $x7 = {e3 82 b8 e3 83 a7 e3 83 83 e3 83 88}
        $x8 = {e5 a4 a9 e4 bd bf}
        $x9 = {e7 b4 ab e9 99 bd e8 8a b1}
        $x10 = {e7 a7 98 e5 af 86 e3 81 ae e7 9a 87 e5 b8 9d}
        $x11 = {82 e7 82 b9 82 f1 8a 4b 92 69}
        $x12 = {83 4a 83 75 83 67 92 8e}
        $x13 = {94 70 9a d0 82 cc 8a 58}
        $x14 = {83 43 83 60 83 57 83 4e 82 cc 83 5e 83 8b 83 67}
        $x15 = {83 68 83 8d 83 8d 81 5b 83 54 82 d6 82 cc 93 b9}
        $x16 = {93 c1 88 d9 93 5f}
        $x17 = {83 57 83 87 83 62 83 67}
        $x18 = {93 56 8e 67}
        $x19 = {8e 87 97 7a 89 d4}
        $x20 = {94 e9 96 a7 82 cc 8d 63 92 e9}
        $x21 = {30 89 30 5b 30 93 96 8e 6b b5}
        $x22 = {30 4b 30 76}
        $x23 = {5e c3 58 9f 30 6e 88 57}
        $x24 = {30 a4 30 c1 30 b8 30 af 30 6e 30 bf 30 eb 30 c8}
        $x25 = {30 c9 30 ed 30 ed 30 fc 30 b5 30 78 30 6e 90 53}
        $x26 = {72 79 75 70 70 b9}
        $x27 = {30 b8 30 e7 30 c3 30 c8}
        $x28 = {59 29 4f 7f}
        $x29 = {7d 2b 96 7d 82 b1}
        $x30 = {79 d8 5b c6 30 6e 76 87 5e 1d}
        $x31 = {2b 4d 49 6b 2d 2b 4d 46 73 2d 2b 4d 4a 4d 2d 2b 6c 6f 34 2d}	
        $x32 = {2b 4d 45 73 2d 2b 4d 48}
        $x33 = {2b 58 73 4d 2d 2b 57 4a 38 2d 2b 4d 47 34 2d 2b}
        $x34 = {2b 4d 4b 51 2d 2b 4d 4d 45 2d 2b 4d 4c 67 2d 2b 4d 4b 38 2d 2b 4d 47 34 2d 2b 4d 4c 38 2d 2b 4d}
        $x35 = {2b 4d 4d 6b 2d 2b 4d 4f 30 2d 2b 4d 4f 30 2d 2b 4d 50 77 2d 2b 4d 4c 55 2d 2b 4d 48 67 2d 2b 4d}
        $x36 = {2b 63 6e 6b 2d 2b 64 58 41 2d 2b 63}
        $x37 = {2b 4d 4c 67 2d 2b 4d 4f 63 2d 2b 4d 4d 4d 2d 2b}
        $x38 = {2b 57 53 6b 2d 2b 54 33}
        $x39 = {2b 66 53 73 2d 2b 6c 6e 30 2d 2b 67}
        $x40 = {2b 65 64 67 2d 2b 57 38 59 2d 2b 4d 47 34 2d 2b 64 6f 63 2d}

        
    condition:
        not (($x1 or $x6 or $x12 or not $x21 or $x32) and ($x3 or $x5 or not $x11 or $x24 or $x35) and (not $x3 or $x31 or $x40 or $x9 or $x27) and ($x4 or $x8 or $x10 or $x29 or $x40) and ($x4 or $x7 or $x11 or $x25 or not $x36) and ($x8 or $x14 or $x18 or $x21 or $x38) and ($x12 or $x15 or not $x20 or $x30 or $x35) and ($x19 or $x21 or not $x32 or $x33 or $x39) and ($x2 or $x37 or $x19 or not $x23) and (not $x5 or $x14 or $x23 or $x30) and (not $x5 or $x8 or $x18 or $x23) and ($x33 or $x22 or $x4 or $x38) and ($x2 or $x20 or $x39) and ($x3 or $x15 or not $x30) and ($x6 or not $x17 or $x30) and ($x8 or $x29 or not $x21) and (not $x16 or $x1 or $x29) and ($x20 or $x10 or not $x5) and (not $x13 or $x25) and ($x21 or $x28 or $x30) and not $x2 and $x3 and not $x7 and not $x10 and not $x11 and $x14 and not $x15 and not $x22 and $x26 and not $x27 and $x34 and $x36 and $x37 and not $x40)
}
