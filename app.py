import openai
from flask import Flask, request, render_template, send_file
import pandas as pd
import io

# Set up the OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define the OpenAI GPT prompt
gpt_prompt = "Can you write me a compelling product description for a product with these features: "

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files["file"]
    if uploaded_file.filename != "":
      
        df = pd.read_excel(uploaded_file)

        # Create a list of row strings, where each row string is a concatenation of the header and corresponding value for ChatGPT to know what to include
        row_strings = []
        for index, row in df.iterrows():
            row_string = ", ".join([f"{header}:{value}" for header, value in zip(df.columns, row)])
            row_strings.append(row_string)

        # Use the OpenAI API to generate responses to each prompt
        response_strings = []
        prompt_strings = []  # In case you'd like to view the prompts that went it as well
        
        for row_string in row_strings:
            prompt = gpt_prompt + row_string  # Concatenate the GPT prompt and the row string
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.5,
            )
            # Play around with the parameters, note that I've personally found that most product descriptions are between 150 and 300 tokens so 500 should be plenty
            
            response_string = response.choices[0].message['content'].strip()
            response_strings.append(response_string)
            prompt_strings.append(prompt) 
            
        # Combine the response strings and prompt strings and write them to a CSV file
        result_strings = [response_string for response_string in response_strings]
        #result_strings = [f"Prompt: {prompt}, Response{response_string}" for prompt, response_string in zip(prompt_strings, response_strings)]
        result_df = pd.DataFrame({"Result": result_strings})
        result_csv = result_df.to_csv(index=False)

        result_bytes = io.BytesIO(result_csv.encode())
        result_bytes.seek(0)
        return send_file(result_bytes, attachment_filename="results.csv", as_attachment=True)

    else:
        return "No file selected."

if __name__ == "__main__":
    app.run()
