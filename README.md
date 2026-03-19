# 🧠 GitHub Profile Viewer
The GitHub Profile Viewer is a web application that allows users to view GitHub profiles and their corresponding data. The application consists of a backend API built using FastAPI and a frontend built using HTML, CSS, and JavaScript. The backend API fetches user data from the GitHub API and returns it to the frontend, which then displays the data to the user. The application provides a simple and intuitive way for users to view GitHub profiles and their associated data.

## 🚀 Features
- **User Profile Viewing**: The application allows users to view GitHub profiles and their corresponding data, including username, name, email, and more.
- **Error Handling**: The application handles errors and returns an error message if the user is not found or if there is an issue with the GitHub API.
- **CORS Support**: The application supports CORS requests, allowing the frontend to make requests to the backend API.
- **Asynchronous Requests**: The application uses asynchronous requests to fetch user data from the GitHub API, improving performance and reducing latency.

## 🛠️ Tech Stack
* **Backend**:
  + FastAPI: A modern, fast (high-performance), web framework for building APIs.
  + httpx: A library for making asynchronous HTTP requests.
  + uvicorn: A ASGI web server for building asynchronous web applications.
* **Frontend**:
  + HTML: The standard markup language for building web applications.
  + CSS (Tailwind CSS): A utility-first CSS framework for building custom user interfaces.
  + JavaScript: A programming language for building dynamic and interactive web applications.
* **Dependencies**:
  + pyproject.toml: A file used to manage the project's dependencies and configuration.
 

### Setup Instructions
1. Clone the repository: 
2. Install The following dependencies: `pip install fastapi uvicorn httpx` and `uvicorn main:app --reload`
3. Start the backend API: `fastapi dev`


## 💻 Usage
1. Open `index.html` file directly from browser
2. Enter a GitHub username in the input field and click the "Fetch User" button
3. The application will fetch the user's data from the GitHub API and display it on the page


## 📂 Project Structure
```markdown
github-profile-viewer/
├── main.py
├── pyproject.toml
├── frontend/
│   ├── index.html
└── README.md
```

## 📸 Screenshots
![alt text](https://github.com/Muneer282/Show-GitHub-Activity-web-app/blob/master/GitHub-Activity-Viewer.png?raw=true)


