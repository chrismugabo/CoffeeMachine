# Coffee Machine Simulator

This project simulates a coffee machine using Python. It allows users to select a drink from a menu, process payment, and simulate the making of the coffee if enough resources are available and the payment is sufficient.

## Features

- **Menu Selection**: Users can choose from a list of available coffee drinks.
- **Payment Processing**: The application accepts coins as payment and calculates if the amount is sufficient for the selected drink.
- **Resource Check**: Before making a coffee, it checks if there are enough resources (water, milk, coffee) available.
- **Reports**: Users can generate reports that show the current resource levels and profits.

## How to Run

1. Ensure you have Python installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run `python main.py` to start the coffee machine simulator.

## Project Structure

- `main.py`: The main script that runs the coffee machine simulator.
- `menu.py`: Contains the `Menu` and `MenuItem` classes that model the coffee menu.
- `money_machine.py`: Contains the `MoneyMachine` class that handles payment processing.
- `coffee_maker.py`: Contains the `CoffeeMaker` class that simulates the coffee making process.

## Dependencies

This project is built using Python 3. No external libraries are required.

## Contributing

Feel free to fork this project and submit a pull request if you have suggestions for improvements.

## License

This project is open source and available under the [MIT License](LICENSE).