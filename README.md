# nerdart


## Nerdy art made with math and code.

```
 _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
/\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\
\/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/
         _             _            _          _            _                   _         _
        /\ \     _    /\ \         /\ \       /\ \         / /\                /\ \      /\ \
       /  \ \   /\_\ /  \ \       /  \ \     /  \ \____   / /  \              /  \ \     \_\ \
      / /\ \ \_/ / // /\ \ \     / /\ \ \   / /\ \_____\ / / /\ \            / /\ \ \    /\__ \
     / / /\ \___/ // / /\ \_\   / / /\ \_\ / / /\/___  // / /\ \ \          / / /\ \_\  / /_ \ \
    / / /  \/____// /_/_ \/_/  / / /_/ / // / /   / / // / /  \ \ \        / / /_/ / / / / /\ \ \
   / / /    / / // /____/\    / / /__\/ // / /   / / // / /___/ /\ \      / / /__\/ / / / /  \/_/
  / / /    / / // /\____\/   / / /_____// / /   / / // / /_____/ /\ \    / / /_____/ / / /
 / / /    / / // / /______  / / /\ \ \  \ \ \__/ / // /_________/\ \ \  / / /\ \ \  / / /
/ / /    / / // / /_______\/ / /  \ \ \  \ \___\/ // / /_       __\ \_\/ / /  \ \ \/_/ /
\/_/     \/_/ \/__________/\/_/    \_\/   \/_____/ \_\___\     /____/_/\/_/    \_\/\_\/
 _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
/\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\
\/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/
```


## Setup

This project requires a conda environment. Use `mkenv.sh` to set it up. See
the help for information on how to run it:

    sh mkenv.sh --help


## Use

First, activate your environment:

    conda activate nerdart

Once activated, everything in this project is accessible via the `nerdart` command.

For example, to display the project's logo:

    nerdart logo

To see all available artworks:

    nerdart ls

Once an artwork is selected, see which options are available for customization:

    nerdart <artwork> --help/-h

To generate the selected artwork:

    nerdart <artwork> [options]

**Note:** All options are optional. If none are passed, the selected artwork
will be generated with all default values.

To create a new artwork `foo` from a template:

    nerdart template foo

This will create a `foo.py` file inside `nerdart/art` with the basic structure
already in place, ensuring compatibility with the `nerdart` package. Once your
artwork is complete, to run it:

    nerdart foo


# Have fun!
