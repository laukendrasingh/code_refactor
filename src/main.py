from ui import render_ui
from api import app

print("Start: code refactor")
render_ui()
print("End: code refactor")

#IT'S NOT USING IN POC. ADDED ONLY FOR LEARNING.
if __name__ == '__main__':
    app.run(debug=True, port=50010, use_reloader=False)
