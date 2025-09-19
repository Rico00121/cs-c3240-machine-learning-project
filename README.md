# S&P500 Prediction with Machine Learning

This project is one part of the course CS-C3240 Machine Learning D at Aalto University.

## Requirements

- Python >= 3.10
- uv (Python package manager)

## Environment Setup

### 1. Install uv

### 2. Clone the repository

### 3. Create virtual environment and install dependencies
```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# or .venv\Scripts\activate  # Windows

# Install all dependencies
uv sync
```

### 4. Register Jupyter kernel (Optional but recommended)
```bash
# Register the virtual environment as a Jupyter kernel
python -m ipykernel install --user \
    --name=machine-learning-env \
    --display-name "CS-C3240"
```

### 5. Start Jupyter Notebook
```bash
jupyter notebook
```

## Main Dependencies

- **jupyter**: Interactive development environment
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **matplotlib**: Basic data visualization
- **seaborn**: Statistical data visualization

## Project Structure

```
machine-learning/
├── pyproject.toml              # Project configuration and dependencies
├── uv.lock                     # Locked dependency versions (ensures consistency)
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── 01_download_data.py         # Step 1: Data download script
├── 02_pre_processing.ipynb     # Step 2: Data preprocessing
├── 03_data_exploration.ipynb   # Step 3: Exploratory data analysis
├── 04_model_training.ipynb                  # Step 4: Model training and evaluation
├── data/                       # Downloaded datasets
└── .venv/                      # Virtual environment (not committed to Git)
```

## Collaborative Development Workflow

This project is developed collaboratively by two team members. To facilitate synchronous development and avoid merge conflicts, we have structured the workflow into numbered sequential notebooks:

### Execution Order
**⚠️ IMPORTANT: Execute files in the following order for proper reproduction:**

1. **01_download_data.py** - Download and organize the dataset
2. **02_pre_processing.ipynb** - Clean and preprocess the data
3. **03_data_exploration.ipynb** - Exploratory data analysis and visualization
4. **04_model_training.ipynb** - Model training, evaluation, and predictions

## Usage

1. **Follow the numbered execution order** (01 → 02 → 03 → 04)
2. Each notebook saves intermediate results for the next step
3. Place data files in the `data/` directory
4. To add new dependencies: `uv add package_name`
5. After updating dependencies, commit both `pyproject.toml` and `uv.lock` files

## Collaboration Guidelines

- **Do NOT commit** `.venv/` virtual environment directory
- **DO commit** `pyproject.toml` and `uv.lock` files
- New collaborators only need to run `uv sync` to get the exact same environment

## Jupyter Kernel Management

If you want to use this environment in Jupyter:

1. **Register kernel** (one-time setup):
   ```bash
   python -m ipykernel install --user --name=machine-learning-env --display-name "CS-C3240"
   ```

2. **Select kernel in Jupyter**: When creating a new notebook, select "CS-C3240" from the kernel dropdown

3. **Remove kernel** (if needed):
   ```bash
   jupyter kernelspec remove machine-learning-env
   ```