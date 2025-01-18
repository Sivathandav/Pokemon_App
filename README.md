# Pokepedia - Pokémon App

Pokepedia is a web-based Pokémon application that allows users to explore, search, and filter Pokémon based on various attributes such as ID, name, type, weight, and height. It provides a clean and responsive design that works across all screen sizes.

## Features

- **Search Pokémon**: Easily find your favorite Pokémon by name.
- **Filter Pokémon**: Sort Pokémon by ID, name, weight, or height, or filter them by type.
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices.
- **Pokémon Grid**: Displays Pokémon in a visually appealing grid layout.
- **Pagination**: Seamless navigation through the Pokémon list with previous and next buttons.

## Screenshots

_Add screenshots of your application here._

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pokemon.git
   ```
2. **Navigate to the Project Directory**:

   ```bash
   cd pokemon
   ```

3. **Install Dependencies**:
   Make sure you have Python installed. Install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Start the Flask development server:

   ```bash
   python app.py
   ```

5. **Access the Application**:
   Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

```plaintext
pokemon/
│
├── static/
│   ├── images/
│   │   └── yellow-mouse-ride-a-ball-background-free-vector.jpg
│   └── css/
│
├── templates/
│   ├── index.html
│   └── details.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `static/`: Contains static files like images and CSS.
- `templates/`: Holds the HTML templates for the application.
- `app.py`: Main application logic.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Documentation for the project.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: PostgreSQL (or any preferred database)

## Future Enhancements

- Add user authentication for personalized Pokémon collections.
- Implement a feature to view detailed Pokémon stats and abilities.
- Allow users to save their favorite Pokémon.
- Integrate Pokémon API for real-time data updates.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or issues, please contact:

- **Name**: Sri Siva Thandavan G
- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)
