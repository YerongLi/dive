from flask import Flask, render_template_string
import os
import threading
import time
import json
import random
import webbrowser

app = Flask(__name__)
start_time_file = 'start_time.json'
countdown_duration = 60 * 60  # 30 minutes in seconds
json_data_file = 'data.json'  # Path to your data.json file

# Global variable to store the generated questions
generated_links = None

def save_start_time():
    with open(start_time_file, 'w') as f:
        json.dump({'start_time': time.time()}, f)

def load_start_time():
    if os.path.exists(start_time_file):
        with open(start_time_file, 'r') as f:
            data = json.load(f)
            return data['start_time']
    return None

def clear_start_time():
    if os.path.exists(start_time_file):
        os.remove(start_time_file)

def shutdown_system():
    time.sleep(countdown_duration)  # Sleep for 30 minutes
    os.system('shutdown now')

def get_random_questions():
    with open(json_data_file, 'r') as f:
        data = json.load(f)
    #c = 1750
    c = 1850
    questions = [item for item in data if c-100 <= item['Rating'] <= c+100]
    random_questions = random.sample(questions, 3)
    with open('random.txt', 'r') as source_file:
        with open('randombak.txt', 'w') as backup_file:
            for line in source_file:
                backup_file.write(line)

    # Append the question links to random.txt
    with open('random.txt', 'a') as file:
        for question in random_questions:
            file.write(f"https://leetcode.com/problems/{question['TitleSlug']}\n")
    
    return [f"https://leetcode.com/problems/{question['TitleSlug']}" for question in random_questions]

@app.route('/')
def home():
    global generated_links

    # Generate the random questions only once
    if generated_links is None:
        generated_links = get_random_questions()

    # Calculate remaining time
    start_time = load_start_time()
    if start_time:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, countdown_duration - elapsed_time)
    else:
        remaining_time = countdown_duration

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LeetCode Links and Countdown</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            .countdown { font-size: 2em; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>LeetCode Links</h1>
        <ul>
            {% for link in links %}
                <li><a href="{{ link }}" target="_blank">{{ link }}</a></li>
            {% endfor %}
        </ul>
        <div class="countdown" id="countdown">Time remaining: {{ remaining_time // 60 }}:{{ remaining_time % 60 }}</div>
        <script>
            var countdownElement = document.getElementById('countdown');
            var timeRemaining = {{ remaining_time }};

            function updateCountdown() {
                var minutes = Math.floor(timeRemaining / 60);
                var seconds = timeRemaining % 60;
                countdownElement.textContent = 'Time remaining: ' + minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
                if (timeRemaining > 0) {
                    timeRemaining--;
                    setTimeout(updateCountdown, 1000);
                } else {
                    localStorage.removeItem('endTime');
                }
            }

            updateCountdown();
        </script>
    </body>
    </html>
    ''', links=generated_links, remaining_time=remaining_time)

if __name__ == '__main__':
    # Clear start time on interrupt
    import signal
    def handle_interrupt(signal, frame):
        clear_start_time()
        os._exit(0)
    signal.signal(signal.SIGINT, handle_interrupt)

    # Save start time and start the shutdown timer in a separate thread
    save_start_time()
    threading.Thread(target=shutdown_system).start()
    webbrowser.open('http://127.0.0.1:5000')
    os.system('git add -u')
    os.system('git push origin master')
    app.run(debug=True)
