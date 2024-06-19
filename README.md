
# Housie

Housie is a full-fledged implementation of the popular game "Housie" (also known as Bingo) with ticket and table generators. This project is built using Python and Flask, and it features a cricket theme.

## Features

- **Ticket Generator**: Generate unique Housie tickets with random numbers.
- **Table Generator**: Generate random tables for the Housie game.
- **Flask Web Application**: The ticket generator and game table are served as Flask web applications for easy access and usage.
- **Cricket Theme**: The game is designed with a cricket theme, adding a fun and engaging twist to the classic Housie experience.

## Installation

1. Clone the repository: `git clone https://github.com/your-repo/housie.git`
2. Navigate to the project directory: `cd housie`
3. Create a virtual environment (optional but recommended): `python3 -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or macOS: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. **Ticket Generator**:
   - Run the ticket generator Flask application: `flask run ticket.py`
   - Access the ticket generator in your web browser at `http://localhost:5000`

2. **Table Generator**:
   - Run the table generator Flask application: `flask run table.py`
   - Access the table generator in your web browser at `http://localhost:5000`

## Repository Structure

- `static/`: Contains static files (e.g., CSS, JavaScript)
- `templates/`: Contains HTML templates
- `ticket.py`: Flask application for the ticket generator
- `table.py`: Flask application for the table generator
- `test.json`, `tick_dicts.json`, `who_won.json`: JSON files for testing and data storage
- `testfile.txt`: Text file for testing
- `README.md`: This file

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to thank the open-source community for the libraries and resources used in this project, as well as our instructors and peers for their guidance and support.
