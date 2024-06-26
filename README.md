# CODE REFACTOR
It's designed to simplify the process of code refactoring. 
It offers a user-friendly interface where users can upload code files then it refactors the code.

### PROJECT SETUP:
1. Checkout source code: https://git.impressicocrm.com/impressico-ai-mgmt/impressico-general/pocs/-/tree/laukendra_singh_code_refactor
2. Create env "python3 -m venv learn-env" and then activate venv "source learn-env/bin/activate"
3. Install dependency: pip3 install -r requirements.txt
4. Run app: streamlit run src/main.py
5. Make sure you have added .env.dev file and added the required api-key

### DOCKER BUILD:
1. Start docker using DockerDesktop
2. Set temporary path: export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"
3. Docker build: sudo docker build -t coderefactor_image .
4. Check coderefactor_image docker image: docker image ls 
5. Create docker volume to store logs: docker volume create coderefactor_log_volume
6. Run docker image: docker run -p 8501:8501 -v coderefactor_log_volume:/data/app.log coderefactor_image
7. OR skip above 5 & 6 points and run app without volume:  docker run -p 8501:8501 coderefactor_image

### DEPLOYE APP ON STREAMLIT:
1. Login on https://share.streamlit.io with your github credentials
2. Create app -> then provide below options to deploy an app
    Repository: laukendrasingh/code_refactor
    Branch: main
    Main file path: src/main.py
    App URL (optional): coderefactor.streamlit.app
    Secrets: put your secrets key-value here as OPEN_AI_KEY="value_here"
3. You should able to see running app on url: https://coderefactor.streamlit.app/
4. Click on 'Manage app' to see the logs

### TOOLS AND TECHNOLOGY:
1. Python: 3.9.6
2. pip3: 21.2.4
3. Visual Studio Code: 1.89.1
4. Docker: 26.1.1

### IMPORTANT LINKS:
1. UI: https://docs.streamlit.io
2. LLM: https://deepinfra.com
4. Code play: https://nb.anaconda.cloud
5. Code deployement: https://share.streamlit.io/
6. Code refactor app: https://coderefactor.streamlit.app/
7. Source code: https://github.com/laukendrasingh/code_refactor

