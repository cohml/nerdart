# `nerdart`


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

The are two ways to use this project:

1. [locally from your primary filesystem](#local-filesystem)

2. [inside a docker container](#docker-container)


### Local filesystem

First use `mkenv.sh` to create the necessary environment. See the help for
information on how to run it:

    ./mkenv.sh --help

After the environment has been created, activate it using `conda activate` as
appropriate for your installation.

The package should now be ready for [use](#use).


### Docker container

First build the docker image with the requisite conda environment installed
inside it:

    docker build . --tag nerdart

After the image has been created, to use the project, run a container:

    docker run -it --rm --publish 80:80 nerdart <subcommand>

The available values for `<subcommand>` are enumerated [below](#use).


## Use

Once your environment is activated or your docker image has been created, you
can access all of this project's capabilities via the `nerdart` command. Each
capability has a dedicated "subcommand" that follows `nerdart`.

For example, to display the project's logo:

    nerdart logo

To see all available artworks:

    nerdart ls

Once an artwork is selected, see which options are available for customization:

    nerdart <artwork> --help/-h

To generate the selected artwork:

    nerdart <artwork> [OPTIONS]

**Note:** All options are optional. If none are passed, the selected artwork
will be generated with all default values.

To create a new artwork `foo` from a template:

    nerdart template foo

This will create a `foo.py` file inside `nerdart/art` with the basic structure
already in place, ensuring compatibility with the `nerdart` package. Once your
artwork is complete, to run it:

    nerdart foo


# Have fun!
