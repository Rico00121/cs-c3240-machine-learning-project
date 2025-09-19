# Machine Learning Project

This is a project repository for Aalto University Machine Learning course CS-CS-C3240.

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
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock            # Locked dependency versions (ensures consistency)
├── README.md           # Project documentation
├── .gitignore         # Git ignore file
├── main.py            # Main program file
└── .venv/             # Virtual environment (not committed to Git)
```

## Usage

1. Conduct all machine learning experiments in Jupyter Notebook
2. Place data files in the `data/` directory
3. To add new dependencies: `uv add package_name`
4. After updating dependencies, commit both `pyproject.toml` and `uv.lock` files

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