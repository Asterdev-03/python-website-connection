# Python-to-Website Value Transfer

This is a simple example of how to send a value from a Python script to a website and display it on the webpage.

### Installation

1. Clone the repository or download the project files.

### Running the Project

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the Python script with the command: `python send_value.py`
3. Open your web browser and navigate to `http://127.0.0.1:5500/index.html`

You should see the value "hi" displayed on the webpage.

## How It Works

The Python script `send_value.py` sets up a simple HTTP server on `http://localhost:8000` and sends the value "hi" when a GET request is received.

The HTML file `index.html` fetches the value from the Python server using the `fetch` API and displays it in an HTML element with the id "value".

