---
name: install-yuexinmiao
description: Install the ready-made Yuexinmiao (月薪喵) custom pet for Codex desktop when the user wants this cat. Reuse the bundled package without generating new art.
---

Use the prebuilt package from https://github.com/miroxsy-oss/yuexinmiao-codex-pet.

If this skill is inside a full checkout, the repository root is two directories above this skill folder. Otherwise download the repository to a temporary directory. Read its README and LICENSE to retain attribution and personal, noncommercial scope.

For an authorized install, run `python scripts/install.py` from the repository root. It verifies the bundled checksums, installs under `$CODEX_HOME/pets` or `~/.codex/pets`, and backs up a different existing copy of the same pet. Installation needs only Python's standard library; Pillow is needed only to rebuild or audit images. Do not regenerate sprites or invoke image generation for a normal install.

Tell the user the installed path and that the pet picker entry is 「月薪喵桌面宠物」. Do not claim the live UI switched unless verified. This package targets Codex desktop custom pets, not a general ChatGPT mobile/web avatar setting.

If the user wants animation changes, consult `source/selection.json` and `docs/SELF_CHECK.md`; preserve their selected actions and report when a request changes the installed artwork.
