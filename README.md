# Flight Ticket Price Prediction

A web application that predicts flight ticket prices using machine learning. Built with FastAPI backend and HTML/CSS/JavaScript frontend.

## Features

- **Real-time Price Prediction**: Uses trained Linear Regression model (90.48% accuracy)
- **User-friendly Interface**: Clean, responsive design with intuitive form
- **Dynamic Options**: Dropdowns populated from the API
- **FastAPI Backend**: RESTful API with automatic documentation
- **Error Handling**: Comprehensive validation and error messages

## Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Scikit-learn**: Machine learning library for the prediction model
- **Pandas**: Data manipulation and analysis
- **Uvicorn**: ASGI server for FastAPI

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Dynamic form handling and API communication

### Model
- **Linear Regression**: Trained on 300,153 flight records
- **Features**: Airline, route, timing, duration, days until flight
- **Accuracy**: 90.48% R² score on test data

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Backend Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd Flight-Ticket-Price-Prediction-Model-main
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Train and save the model**
```bash
python train_model.py
```

4. **Start the FastAPI server**
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

1. **Start the frontend server**
```bash
python server.py
```

## Usage

1. **Access the application**
   - Frontend: http://localhost:3000
   - API Documentation: http://localhost:8000/docs

2. **Fill in flight details**
   - Select airline, source/destination cities
   - Choose departure/arrival times
   - Enter flight number, duration, days until flight
   - Select class and number of stops

3. **Get prediction**
   - Click "Predict Price" to get the estimated ticket price
   - Results shown in Indian Rupees (INR)

## API Endpoints

### Prediction
- **POST** `/predict` - Predict flight price
- **GET** `/` - API health check

### Dropdown Options
- **GET** `/airlines` - Available airlines
- **GET** `/cities` - Available cities
- **GET** `/departure_times` - Departure time options
- **GET** `/arrival_times` - Arrival time options
- **GET** `/stops` - Number of stops options
- **GET** `/classes` - Travel class options

## Model Details

### Dataset
- **Size**: 300,153 flight records
- **Features**: 11 predictive features
- **Target**: Flight ticket price (INR)

### Features Used
1. Airline (categorical)
2. Flight number (categorical)
3. Source city (categorical)
4. Destination city (categorical)
5. Departure time (categorical)
6. Arrival time (categorical)
7. Number of stops (categorical)
8. Travel class (categorical)
9. Flight duration (continuous)
10. Days until departure (continuous)

### Model Performance
- **Linear Regression**: 90.48% R² score
- **Random Forest**: 90.24% R² score
- **Decision Tree**: 86.05% R² score

## File Structure

```
Flight-Ticket-Price-Prediction-Model-main/
├── main.py                 # FastAPI application
├── train_model.py          # Model training script
├── server.py               # Frontend server
├── requirements.txt        # Python dependencies
├── model.pkl              # Trained model file
├── label_encoders.pkl     # Categorical encoders
├── public/
│   └── index.html         # Frontend application
├── src/
│   ├── App.js            # React app component
│   ├── App.css           # App styles
│   ├── index.js          # React entry point
│   └── index.css         # Global styles
└── Flight-Ticket-Price-Prediction-Model-main/
    ├── Flight_ticket_price_prediction.ipynb  # Original notebook
    ├── flight ticket price prediciton dataset.csv  # Dataset
    └── Flight ticket price prediction.pdf  # Documentation
```

## Development

### Adding New Features
1. Modify the model in `train_model.py`
2. Update API endpoints in `main.py`
3. Enhance frontend in `public/index.html`

### Training New Model
```bash
python train_model.py
```
This will:
- Load the dataset
- Train the Linear Regression model
- Save model and encoders to disk

### API Documentation
Visit http://localhost:8000/docs for interactive API documentation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Please ensure compliance with data usage policies and licensing requirements.

## Troubleshooting

### Common Issues

1. **Model files not found**
   - Run `python train_model.py` to generate model files

2. **Port already in use**
   - Change port numbers in the startup commands
   - Kill existing processes using the ports

3. **Dependencies missing**
   - Install with `pip install -r requirements.txt`

4. **CORS errors**
   - Ensure backend is running before accessing frontend
   - Check that both servers are on correct ports

### Getting Help

- Check the API documentation at http://localhost:8000/docs
- Verify all dependencies are installed
- Ensure both servers are running simultaneously

## Future Enhancements

- [ ] Add more machine learning models
- [ ] Implement user authentication
- [ ] Add historical price trends
- [ ] Include price comparison features
- [ ] Mobile app development
- [ ] Real-time flight data integration
