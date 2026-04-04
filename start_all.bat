@echo off
echo Starting Gigshield Project Setup...

:: Start the ML API (Python)
echo Starting ML API on port 5000...
start "Gigshield ML API" cmd /c "cd ml && python app.py"

:: Set JAVA_HOME correctly for this environment and start the Backend
echo Starting Spring Boot Backend on port 8080...
set "JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-21.0.10.7-hotspot"
start "Gigshield Backend" cmd /c "cd backend && mvnw.cmd spring-boot:run"

:: Start the Frontend (Vite)
echo Starting Frontend on port 5173...
start "Gigshield Frontend" cmd /c "cd frontend && npm run dev"

echo Process started!
echo Frontend: http://localhost:5173
echo Backend:  http://localhost:8080
echo ML API:   http://localhost:5000

