# Vacation Management System

A Python-based system for managing vacation packages, user accounts, and social features like liking vacation packages. This system uses a facade design pattern to provide a simplified interface for complex subsystem interactions.

## 🌟 Features

### User Management
- User registration with validation
- Secure login system
- Profile management
- Role-based access control

### Vacation Package Management
- Create new vacation packages
- View all available vacations
- Edit existing vacation details
- Delete vacation packages
- Support for multiple countries
- Price range management
- Date validation for vacation periods

### Social Features
- Like/Unlike vacation packages
- View liked vacations
- Track total likes per vacation
- User engagement metrics

## 🔧 Technical Architecture

The project follows a layered architecture with clear separation of concerns:

### Facade Layer
- `SystemFacade`: Main system interface
- `UserFacade`: User management interface
- `VacationFacade`: Vacation management interface

### Business Logic Layer
- `UserLogic`: User-related business rules
- `VacationLogic`: Vacation-related business rules
- `LikeLogic`: Social features logic
- `CountryLogic`: Country management logic

### Data Access Layer
- Uses a DAL (Data Access Layer) class for database operations
- Supports MySQL database interactions
- Transaction management

## 💻 Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vacation-management-system.git
cd vacation-management-system
```

2. Configure your database:
- Create a MySQL database named `vacation_system`
- Update database credentials in your configuration

3. Initialize the database schema:
- Run the provided SQL scripts to create necessary tables

## 🗄️ Database Schema

The system uses the following main tables:
- `users`: User account information
- `vacations`: Vacation package details
- `likes`: User-vacation like relationships
- `countries`: Available countries for vacations

## 🚀 Usage

### User Operations
```python
from facade.user_facade import UserFacade

user_facade = UserFacade()
# Register new user
user_facade.add_user()
# Login
user_facade.login()
```

### Vacation Management
```python
from facade.vacation_facade import VacationFacade

vacation_facade = VacationFacade()
# Add new vacation
vacation_facade.add_vacation()
# View all vacations
vacation_facade.view_all_vacations()
```

### Social Interactions
```python
from facade.system_facade import SystemFacade

system = SystemFacade()
# Like a vacation
system.like_vacation()
# View liked vacations
system.view_liked_vacations()
```

## ✅ Input Validation

The system includes comprehensive validation for:
- Email format
- Password strength (minimum length, required characters)
- Date formats and ranges
- Price ranges
- Country existence
- URL formats for images

## 🔒 Security Features

- Password validation and security checks
- Session management
- Input sanitization
- Role-based access control



Each module also includes standalone test cases that can be run directly:
```python
python src/facade/system_facade.py
python src/facade/user_facade.py
python src/facade/vacation_facade.py
```

## 📝 Requirements

- Python 3.8+
- MySQL database
- Required Python packages:
  - tabulate
  - mysql-connector-python
  - other dependencies listed in requirements.txt
    

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Guy Bachar
- Tamir Ben David

## 🙏 Acknowledgments

- Thanks to all contributors, 
      AND MOSTLY TO URI SHAMIR
