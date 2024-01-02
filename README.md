## Setup

### Install Docker

<ul>
    <li> (Mac, Linux) Follow the [installation instructions](https://docs.docker.com/get-docker/) </li>
    <li>(Windows):
        <ul>
         <li>Follow the manual installation steps for Windows Subsystem for Linux [here](https://docs.microsoft.com/en-us/windows/wsl/install). On step 1, follow the recommendation of updating to WSL 2. On step 6, you can download Ubuntu 18.04 LTS. You do not necessarily need to install Windows Terminal. </li>
            <li>Now go [here](https://docs.docker.com/desktop/windows/install/) and follow the "Install Docker Desktop on Windows" instructions. You can then start Docker Desktop and follow the quick start quide.</li>
            </ul>
            </li>
            </ul>

### Install VS Code.

Select File -> Open and select *the entire folder*.

VS Code will propose to install "Dev Container". Click "install".

VS Code will give you a message similar to:

> Folder contains a Dev Container configuration file. Reopen folder to develop in a container.

Select "Reopen in container".

Now you should have the folder open while VS Code is in "container development mode".

Create a new terminal using Terminal -> New Terminal.

Run the following:

    act4e-check TestSimpleIntro

This will have created a file `out-results/result-TestSimpleIntro.html`.

From the file tree to the left, right-click the file and select "open preview". You will see the results of the testing.

Now browse the Python files in `src/`. Verify that autocompletion works..

### Sandbox

We provide for you a sandbox, to be able to interact with test cases in a non-obfuscated way. To use it, first check that you have implementations of the objects of interest (e.g. `MyFiniteSet`) are in `act4e_solutions`.

1. Run `cd src.`
2. Run `python -m sandbox.FiniteRelationsProperties`, or `sandbox.FinitePosetRepresentation`, or another one that interests you.
