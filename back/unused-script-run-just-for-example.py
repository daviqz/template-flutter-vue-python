import subprocess

def start_flask():
    try:
        subprocess.run(["flask", "--app", "src/server/server", '--debug', "run"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error on Flask server: {e}")

if __name__ == "__main__":
    start_flask()