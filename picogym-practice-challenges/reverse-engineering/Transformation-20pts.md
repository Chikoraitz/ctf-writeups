# Description

> AUTHOR: MADSTACKS
>
> #### Description
>
> I wonder what this really is... [enc](https://mercury.picoctf.net/static/77a2b202236aa741e988581e78d277a6/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`



# Footprinting

The content of the `enc` file provided is:

`灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽`

The *Python* code provided uses the string built-in function `join` over an array of characters resultant from a bitwise manipulation. The origin of the characters is the variable `flag`. Basically, the code iterates over all characters of `flag` to create a new set of characters that consist of the summation of a byte shifted version of the first character, with the other character in each consecutive pair.

Setting the content provided in the `enc` file as the content of `flag`, the *Python* interpreter raises a `ValueError`:

```bash
Python 3.10.12 (<SNIP>) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"
>>> ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
ValueError: chr() arg not in range(0x110000)
```

The error and *Python* code might indicate that a different text encoding scheme should be applied.



# Representation of textual data

In typography, any *specific shape, design, or representation or a character* is called a **glyph**. In some cases, a character might be represented by more than one glyph, or sometimes, a glyph might represent more than one character. In fonts, glyphs is what fill each slot of the font, e.g., `Times Bold` and `Verdana Italic` each have a unique glyph for the **grapheme** `T`. A grapheme is the smallest functional unit of a writing system, and in most cases, it is synonymous with a character. In some alphabets, like the *Latin* except English, it was necessary to distinguish particular sound mutations, hence, creating the concept of a **diacritic**. A diacritic is glyph add to a base glyph, e.g., `a` - `à`. Some diacritics, such as the acute (`á`) , grave (`à`), and circumflex ⟨`â`⟩ (all shown above an `a`), are often called *accents*. Diacritics may appear above or below a letter or in some other position such as within the letter or between two letters.

**Unicode** is a specification that aims to list every grapheme used by human languages, hence, Unicode specifications are continually revised and updated to add new languages and symbols. The Unicode standard describe how graphemes/characters ought to be represented by **code points**. A code point value is an **integer** in the range `0` to `0x10FFFF`. A code point is written using the notation `U+265E` to represent the character ‘BLACK CHESS KNIGHT’ (`♞`).



## `UTF-8`

The sequence of code points needs to be represented in memory as a set of **code units**, and code units are then mapped to 8-bit bytes. The rules for translating a Unicode string/point into a sequence of bytes are called a **character encoding**, or just an encoding.

The most common and convenient encoding scheme is `UTF-8`. It is also the encoding scheme used by default in *Python*. `UTF` stands for *Unicode Transformation Format*, and the `-8` means that 8-bit values are used in the encoding. `UTF-8` uses the following rules:

- If the code point is < 128 (`U+0000` to `U+007F`), it’s represented by the corresponding byte value.

- If the code point is >= 128, it’s turned into a sequence of two, three, or four bytes, where each byte of the sequence is between 128 and 255.

  | First code point | Last code point | Byte 1     | Byte 2     | Byte 3     | Byte 4     |
  | ---------------- | --------------- | ---------- | ---------- | ---------- | ---------- |
  | `U+0000`         | `U+007F`        | `0xxxxxxx` |            |            |            |
  | `U+0080`         | `U+07FF`        | `110xxxxx` | `10xxxxxx` |            |            |
  | `U+0800`         | `U+FFFF`        | `1110xxxx` | `10xxxxxx` | `10xxxxxx` |            |
  | `U+10000`        | `U+10FFFF`      | `11110xxx` | `10xxxxxx` | `10xxxxxx` | `10xxxxxx` |



## Challenge context

The `UTF-8` binary representation of the file content can be seen with `flag.encode()`:

```bash
>>> flag.encode()
b'\xe7\x81\xa9\xe6\x8d\xaf\xe4\x8d\x94\xe4\x99\xbb\xe3\x84\xb6\xe5\xbd\xa2\xe6\xa5\xb4\xe7\x8d\x9f\xe6\xa5\xae\xe7\x8d\xb4\xe3\x8c\xb4\xe6\x91\x9f\xe6\xbd\xa6\xe5\xbc\xb8\xe5\xbc\xb7\xe3\x95\xa4\xe3\x90\xb8\xe3\xa4\xb8\xe6\x89\xbd'
```

Or: 

```bash
$ echo -n "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽" | hexdump -C
00000000  e7 81 a9 e6 8d af e4 8d  94 e4 99 bb e3 84 b6 e5  |................|
00000010  bd a2 e6 a5 b4 e7 8d 9f  e6 a5 ae e7 8d b4 e3 8c  |................|
00000020  b4 e6 91 9f e6 bd a6 e5  bc b8 e5 bc b7 e3 95 a4  |................|
00000030  e3 90 b8 e3 a4 b8 e6 89  bd                       |.........|
00000039
```

According to the binary `UTF-8` table, each grapheme representation has a 3-byte representation, since the beginning of each character starts with `Ex` (`1110 xxxx`).  



# Solution

The *Unicode* code points of the characters is the following:

```bash
>>> [ord(i) for i in flag]
[28777, 25455, 17236, 18043, 12598, 24418, 26996, 29535, 26990, 29556, 13108, 25695, 28518, 24376, 24375, 13668, 13368, 14648, 25213]
>>> len([ord(i) for i in flag])
19
```

```bash
>>> [ord(i) for i in "picoCTF{"]
[112, 105, 99, 111, 67, 84, 70, 123]
>>> [hex(ord(i)) for i in "picoCTF{"]
['0x70', '0x69', '0x63', '0x6f', '0x43', '0x54', '0x46', '0x7b']
```

Now the goal is to match a binary encoding scheme to which the *Unicode* code point translates the ones that match the known part of the flag string `picoCTF{`. After testing several encoding schemes in *CyberChef*, the answer is the `UTF-16BE` text encoding.

```bash
>>> "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽".encode("utf-16-be")
b'picoCTF{<REDACTED>}'
```

