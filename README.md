# ai-product-descriptions
A Flask web application that uses the ChatGPT API to generate compelling product descriptions for your products based on your product data.

# What is this about
Copywriting isn't for everyone, luckily ChatGPT and the awesome people at OpenAI have made it so that anyone can start generating compelling copy within seconds. This small application takes your product data and runs it through the ChatGPT API to generate product descriptions for your products. There are a lot of tools available right now that provide a similar service, but all of them come at a price tag. This light-version so to speak makes it so that you'd only have to pay for access to the API. This way, any small ecommerce business can now also benefit from leveraging AI to generate compelling copy for your products in no-time!

# Features
* Upload an Excel file with product data to generate product descriptions using OpenAI's ChatGPT (GPT-3.5-turbo).
* Download a CSV file containing the generated product descriptions.
* Easy-to-use web interface built with Flask.
* Secure file handling and storage with Python's io module.
* Easy to install and run locally or deploy to a cloud server.

# Installation
* Clone the repository or download the ZIP file and extract it to a local directory
* Install the required Python packages using pip install
* Make sure you can access your OpenAPI API-key through your account

# Usage
1. Make sure you have the necessary packages installed by running pip install spotipy.
2. Download and save the file in your working directory.
3. Set your API Key. 
4. Make sure your upload file is an Excel file with the first row as a header specifying the product feature (e.g. 'Colour: Red')
5. Note that the parameters for the API call will differ based on the number of product features per product, best advice is to be conservative with the 'Tokens' parameter.
6. After generating the file will automatically download as a CSV to your machine.


# Future
In the future OpenAPI will release better and more advanced language models closer to AGI, make sure to stay up-to-date and update this code with new API's when they come available to generate even better product descriptions.

# Documentation
For more info and documentation on OpenAI please refer to https://platform.openai.com/docs/introduction
