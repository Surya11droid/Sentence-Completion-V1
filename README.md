# RNN_DASH

An interactive dashboard for an RNN/LSTM text prediction model — quick to run locally and easy to extend.

## Features

- Pretrained `lstm_model.h5` included for quick demos
- Minimal dependencies and straightforward local setup
- Example notebook and helper scripts to retrain or update the model


## Quick Start

1. Create a Python virtual environment and activate it.

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Windows CMD
.\.venv\Scripts\activate.bat
```

2. Install dependencies.

```bash
pip install flask tensorflow pandas numpy
```

3. Run the app from the folder.

```powershell
python app.py
# then open http://127.0.0.1:8050 in your browser
```

## Files

- `app.py` — Dash app entrypoint
- `lstm_model.h5` — pretrained model used by the dashboard
- `codefile.ipynb` — experimentation and training notes

## Usage

1. Start the app (see Quick Start).
2. Enter a prompt in the text box and request prediction.
3. The model returns the most likely next words and probabilities.

## Retraining

If you want to retrain the model, open `codefile.ipynb` and follow the notebook cells. After retraining, export the new model as `lstm_model.h5` and replace the existing file.

## Troubleshooting

- If TensorFlow fails to install on Windows, try a specific wheel for your Python version or use `pip install --upgrade pip setuptools wheel` first.
- If the app port 8050 is busy, set the environment variable `PORT` or edit `app.py` to change the port.

## Contributing

Contributions are welcome — open an issue or submit a PR with improvements or model updates.


---

Enjoy exploring the RNN dashboard — ask if you want a README tailored to deployment (Docker/Gunicorn) or a CI-friendly requirements file.
