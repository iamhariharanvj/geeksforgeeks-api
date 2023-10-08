# GeeksforGeeks API

A simple Flask API that retrieves information about a GeeksforGeeks user, including their coding scores and solved problems in various categories.

## Table of Contents

- [Usage](#usage)
- [Local Deployment](#local-deployment)
- [API Endpoints](#api-endpoints)
- [Example](#example)
- [Contributing](#contributing)

## Usage

To use this API, make GET requests to the following endpoint:

```
https://geeksforgeeks-api.vercel.app/get/<username>
```

Replace `<username>` with the GeeksforGeeks username you want to fetch data for.

## Local Deployment

To run this Flask API locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/iamhariharanvj/geeksforgeeks-api.git
   ```

2. Change to the project directory:

   ```bash
   cd geeksforgeeks-api
   ```

3. Create a virtual environment (Python 3.7+ recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the Flask development server:

   ```bash
   python app.py
   ```

7. The API should now be running locally. Access it at:

   ```
   http://localhost:5000/get/<username>
   ```

   Replace `<username>` with the GeeksforGeeks username you want to fetch data for.

## API Endpoints

### Get GeeksforGeeks User Data

- **URL:** `/get/<username>`
- **Method:** GET
- **Parameters:**
  - `username` (string): The GeeksforGeeks username for which you want to fetch data.
- **Response:**

  - If the user exists, it returns a JSON object containing the user's coding scores and solved problems in different categories. Here's an example response:

    ```json
    {
      "username": "hariharanvj2003",
      "overall coding score": 200,
      "total problems solved": 50,
      "monthly coding score": 30,
      "problems": {
        "school": {
          "count": 50,
          "problems": [
            { "question": "Problem 1", "link": "https://example.com/problem1" },
            { "question": "Problem 2", "link": "https://example.com/problem2" }
          ]
        },
        "basic": {
          "count": 40,
          "problems": [
            { "question": "Problem 3", "link": "https://example.com/problem3" },
            { "question": "Problem 4", "link": "https://example.com/problem4" }
          ]
        },
        "easy": {
          "count": 30,
          "problems": [
            { "question": "Problem 5", "link": "https://example.com/problem5" },
            { "question": "Problem 6", "link": "https://example.com/problem6" }
          ]
        },
        "medium": {
          "count": 50,
          "problems": [
            { "question": "Problem 7", "link": "https://example.com/problem7" },
            { "question": "Problem 8", "link": "https://example.com/problem8" }
          ]
        },
        "hard": {
          "count": 30,
          "problems": [
            { "question": "Problem 9", "link": "https://example.com/problem9" },
            {
              "question": "Problem 10",
              "link": "https://example.com/problem10"
            }
          ]
        }
      }
    }
    ```

  - If the user doesn't exist or there is an error, it returns a JSON object with an error message.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit pull requests with your enhancements. I would highly appreciate it
