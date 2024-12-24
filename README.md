# Grievance Handling System

## Description
The Grievance Handling System is a web-based application designed to streamline the process of lodging, managing, and resolving grievances efficiently. Built using Python and Django, the system offers features such as secure user authentication, a dynamic grievance submission form with fields like title, description, priority, and file attachments, and a structured complaint tracking mechanism. Users can easily submit their grievances and track their status, while administrators can manage and address complaints through a dedicated dashboard. With its user-friendly interface and role-based access control, the system ensures a seamless and secure grievance management experience for both users and administrators.

## Installation Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/grievance-handling-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd grievance-handling-system
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Register a new user account or log in with an existing account.
3. Submit a new grievance through the submission form.
4. Track the status of your grievances through the user dashboard.
5. Administrators can log in to the admin dashboard to manage and resolve grievances.

## Outputs
- Users can view the status of their submitted grievances.
- Administrators can view and manage all submitted grievances.

### Example Outputs
!Login Interface
!Sign Up Interface
!Complaint Management System
!Complaint Table
!Complaint Details
!Provide Feedback

## Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
