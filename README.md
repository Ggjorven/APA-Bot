# APA-Bot

**APA-Bot** is a discord bot to help with creating a sources list, by installing it to your discord server.

## Features

- Convert links to APA style.

## Getting Started

### Prerequisites

- C++20 compatible compiler

## Installation

### Windows

1. Clone the repository:
    ```sh
    git clone --recursive https://github.com/ggjorven/APA-Bot.git
    cd APA-Bot
    ```

2. Navigate to the scripts folder:
    ```sh
    cd scripts/windows
    ```

4. Choose what you want it build to:
    - Visual Studio 17 2022:
        ```sh
        ./gen-vs2022.bat
        ```
    - MinGW make files:
        ```sh
        ./gen-make.bat
        ```

### Linux

1. Clone the repository:
    ```sh
    git clone --recursive https://github.com/ggjorven/APA-Bot.git
    cd APA-Bot
    ```

2. Navigate to the scripts folder:
    ```sh
    cd scripts/linux
    ```

3. (Optional) If you haven't already installed the premake5 build system you can install it like this:
    ```sh
    chmod +x install-premake5.sh
    ./install-premake5.sh
    ```

5. Generate make files:
    ```sh
    chmod +x gen-make.sh
    ./gen-make.sh
    ```

## Building

### Windows
- Visual Studio 17 2022:
    1. Navigate to the root of the directory
    2. Open the Pulse.sln file
    3. Start building in your desired configuration
    4. Build files can be in the bin/%Config%-windows/Bot/ folder.
    5. (Optional) Open a terminal and run the Bot project:

        ```sh
        ./Bot.exe
        ```

- MinGW Make:
    1. Navigate to the root of the directory
    2. Open a terminal.
    3. Call make with desired configuration (debug, release):

        ```sh
        make config=release
        ```

    5. Build files can be in the bin/%Config%-windows/Bot/ folder.
    6. (Optional) Open a terminal and run the Bot project:
        ```sh
        ./Bot.exe
        ```

### Linux

1. Navigate to the root of the directory
2. Open a terminal
3. Call make with desired configuration (debug, release):

    ```sh
    make config=release
    ```

5. Build files can be in the bin/%Config%-linux/Bot/ folder.
6. (Optional) Open a terminal and run the Bot project:

    ```sh
    chmod +x Bot
    ./Bot
    ```

## License
This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE.txt) for details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Third-Party Libraries
  - `D++` [https://github.com/brainboxdotcc/DPP.git](https://github.com/brainboxdotcc/DPP.git)
