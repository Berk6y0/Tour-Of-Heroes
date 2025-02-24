Preview of Tour of Heroes
![image](https://github.com/user-attachments/assets/c56e8ca8-fc26-45fa-93d9-388c5c058c8b)
![image](https://github.com/user-attachments/assets/a50b81be-4774-4bde-844b-5a611f32487f)
![image](https://github.com/user-attachments/assets/82de64a6-7bc3-4958-a14b-c1ed09665dbb)
# Tour of Heroes

## Overview
Tour of Heroes is a Single Page Application (SPA) built with Angular for managing heroes. It allows users to create, update, delete, and view details of heroes. Additionally, this version includes image upload functionality for heroes and uses a Flask backend with CORS support.

## Features
- CRUD operations for heroes (Create, Read, Update, Delete)
- Image upload for heroes
- RESTful API with Flask backend
- CORS enabled for frontend-backend communication
- Responsive UI with Angular Material

## Technologies Used
- **Frontend:** Angular, TypeScript, Angular Material
- **Backend:** Flask, Python, Flask-CORS
- **Database:** SQLite (or any preferred database)
- **Image Storage:** Local storage or cloud-based solutions

## Installation & Setup

### Backend (Flask API)
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/tour-of-heroes.git
   cd tour-of-heroes/backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```sh
   python app.py
   ```

### Frontend (Angular App)
1. Navigate to the frontend folder:
   ```sh
   cd ../frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Run the Angular development server:
   ```sh
   ng serve
   ```
4. Open the app in your browser at `http://localhost:4200`.

## API Endpoints
### Heroes Management
- `GET /heroes` - Retrieve all heroes
- `POST /heroes` - Add a new hero
- `GET /heroes/{id}` - Retrieve a hero by ID
- `PUT /heroes/{id}` - Update a hero
- `DELETE /heroes/{id}` - Delete a hero

### Image Upload
- `POST /upload` - Upload an image for a hero

## Example Request
### Uploading a Hero Image
```sh
curl -X POST http://localhost:5000/upload -F "file=@hero.jpg"
```

## CORS Configuration
Flask-CORS is used to allow cross-origin requests from the Angular frontend. This is configured in `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

## Contributing
Feel free to fork this repository and contribute! Open a pull request for review.





