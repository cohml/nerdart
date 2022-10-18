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

![alt text](https://github.com/cohml/nerdart/blob/main/img/default/willy_wonka,quiet=True,n_periods=3,density=1000,resolution=200,color=rainbow,fade=False.png)


## Setup

This project requires a conda environment. To set it up:

    sh mkenv.sh



## Use

First, activate your environment:

    conda activate nerdart

Once activated, everything in this project is accessible via the `nerdart` command.

For example, to display the project's logo:

    nerdart logo

To see all available artworks:

    nerdart ls

Once an artwork is selected, see which options are available for it customizing it:

    nerdart <artwork> --help

Equivalently:

    nerdart <artwork> -h

To generate the artwork:

    nerdart <artwork> [options]

Note that all options are optional. If none are passed, the selected artwork
will be generated with all default values.


# Have fun!
