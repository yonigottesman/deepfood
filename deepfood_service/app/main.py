from app import app

# The following code is for debugging the app localy,
# I dont need it for running with docker
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8118)