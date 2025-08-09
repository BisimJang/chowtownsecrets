# ChowTown API

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create .env file:
   - Copy `.env.example` to `.env`
   - Fill in your environment variables

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

The API will be available at `http://localhost:8000/api/`

Main endpoints:
- `api/recipes/` - List all recipes
- `api/recipes/<id>/` - Get specific recipe
- `api/recipes/create/` - Create new recipe
- `api/recipes/<id>/edit/` - Edit/Delete recipe
- `api/recipes/<recipe_id>/reviews/` - Get recipe reviews
- `api/recipes/<recipe_id>/create-review/` - Create review
### Authentication Endpoints
- `api/auth/` - Base authentication endpoints including:
  - `api/auth/login/` - User login
  - `api/auth/logout/` - User logout
  - `api/auth/password/reset/` - Request password reset
  - `api/auth/password/reset/confirm/<uidb64>/<token>/` - Confirm password reset

### Registration
- `api/auth/registration/` - User registration endpoints

### JWT Token Endpoints
- `api/token/` - Obtain JWT token pair
- `api/token/refresh/` - Refresh JWT token

### API Documentation
- `swagger/` - Swagger UI documentation
- `redoc/` - ReDoc documentation
- `swagger.json` - Raw API schema

### Main Application Endpoints
- `admin/` - Django admin interface
- Recipes endpoints (detailed in swagger documentation)

## Authentication Flow

1. **Registration**:
   ```http
   POST /api/auth/registration/
   {
     "username": "user",
     "password1": "your_password",
     "password2": "your_password"
   }
   ```

2. **Login and Get Token**:
   ```http
   POST /api/token/
   {
     "username": "user",
     "password": "your_password"
   }
   ```
   Response will include `access` and `refresh` tokens

3. **Using the API**:
   Add the access token to all protected requests:
   ```http
   Authorization: Bearer <your_access_token>
   ```

4. **Refresh Token**:
   When access token expires (15 minutes), get a new one:
   ```http
   POST /api/token/refresh/
   {
     "refresh": "<your_refresh_token>"
   }
   ```

5. **Password Reset**:
   - Request reset: `POST /api/auth/password/reset/`
   - Confirm reset: `POST /api/auth/password/reset/confirm/<uidb64>/<token>/`

## Development URLs
- API Base URL: `http://localhost:8000/`
- Admin Interface: `http://localhost:8000/admin/`
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Authentication

This API uses JWT authentication:
- Token URL: `api/auth/jwt/create/`
- Refresh URL: `api/auth/jwt/refresh/`
- Token lifetime: 15 minutes
- Refresh token lifetime: 7 days

## Documentation

- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## CORS

CORS is currently enabled for all origins. Frontend can connect from any domain in development.