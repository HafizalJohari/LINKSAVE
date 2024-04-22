# Bookmarking App

This is a web application that allows users to save links for later reading. It provides features such as pasting links to automatically save them, generating thumbnail previews of saved pages, organizing links with categories/tags, and search functionality. The app also supports syncing across devices, offline access to saved pages, and sharing and collaboration options.

## Overview

The application is built using Python and Flask for the backend, and a suitable frontend framework (e.g., React, Angular, or Vue.js) for the frontend. It uses SQLite as the database to store links, thumbnails, categories/tags, and user information.

## Installation

1. Clone the repository:
git clone https://github.com/your-username/bookmarking-app.git
2. Change into the project directory:
cd bookmarking-app
3. Create a virtual environment:
python3 -m venv venv
4. Activate the virtual environment:
source venv/bin/activate
5. Install the required packages:
pip install -r requirements.txt
6. Set the environment variables:
export SECRET_KEY='your-secret-key'
export DATABASE_URL='sqlite:///app.db'
7. Run the application:
flask run 

## Usage

1. Register or log in to the application.
2. Paste a link in the input field and click "Save" to save the link.
3. View your saved links on the dashboard.
4. Organize links using categories/tags.
5. Search for links using the search bar.
6. Share links with other users.

## Features

- Paste links to automatically save them
- Generate thumbnail previews of saved pages
- Organize links with categories/tags and search functionality
- Sync across devices (web, mobile, desktop)
- Offline access to saved pages
- Sharing and collaboration options

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to contribute to the project.

## License

The project is licensed under the MIT License.
