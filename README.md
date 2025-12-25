# PyTorch Transformer Implementation

A bottom-up PyTorch implementation of the Transformer architecture, designed for training and deploying modern deep learning models.

## Project Structure

```
pytorch-transformer-implementation/
├── src/pytorch_transformer/      # Main source code package
│   ├── models/                   # Model implementations
│   ├── data/                     # Data loading and preprocessing
│   ├── training/                 # Training loops and trainers
│   ├── inference/                # Inference pipelines and serving
│   └── utils/                    # Utility functions and helpers
├── configs/                      # Configuration files
├── data/                         # Dataset storage
│   ├── raw/                      # Original, immutable data
│   ├── processed/                # Cleaned, transformed data
│   └── external/                 # Third-party data sources
├── notebooks/                    # Jupyter notebooks for exploration
├── scripts/                      # Executable scripts
├── tests/                        # Test suite
│   ├── unit/                     # Unit tests
│   └── integration/              # Integration tests
├── docs/                         # Documentation
├── deploy/                       # Deployment configurations
│   ├── docker/                   # Docker configurations
│   └── kubernetes/               # Kubernetes manifests
├── pyproject.toml                # Project dependencies and metadata
├── .gitignore                    # Git ignore rules
├── LICENSE                       # MIT License
└── README.md                     # This file
```

## Directory Descriptions

### `src/pytorch_transformer/`
The main source code package containing all the core functionality:
- **models/**: Transformer model implementations, attention mechanisms, and model components
- **data/**: Dataset classes, data loaders, tokenizers, and preprocessing pipelines
- **training/**: Training loops, optimizers, learning rate schedulers, and training utilities
- **inference/**: Inference pipelines, model serving utilities, and prediction functions
- **utils/**: Common utilities, logging, configuration management, and helper functions

### `configs/`
Configuration files for different aspects of the project:
- Model architecture configurations (e.g., number of layers, hidden dimensions)
- Training hyperparameters (e.g., learning rate, batch size, epochs)
- Data processing configurations (e.g., tokenization settings, data augmentation)

Configuration files typically use YAML format for easy editing and version control.

### `data/`
Storage for datasets used in training and evaluation:
- **raw/**: Original, immutable data dumps - never modify these files
- **processed/**: Cleaned and transformed data ready for model consumption
- **external/**: Data from third-party sources or external APIs

**Note**: Large datasets should be stored externally (e.g., cloud storage) and referenced in config files.

### `notebooks/`
Jupyter notebooks for interactive exploration and experimentation:
- Data exploration and analysis
- Model prototyping and experimentation
- Results visualization and reporting
- Tutorial notebooks

### `scripts/`
Executable Python scripts for common tasks:
- `train.py`: Main training script for model training
- `evaluate.py`: Model evaluation and benchmarking
- `infer.py`: Run inference on new data
- `preprocess_data.py`: Data preprocessing pipeline

### `tests/`
Test suite ensuring code quality and correctness:
- **unit/**: Unit tests for individual functions and classes
- **integration/**: Integration tests for component interactions
- **conftest.py**: Shared pytest fixtures and configuration

### `docs/`
Project documentation:
- API documentation (auto-generated from docstrings)
- User guides and tutorials
- Architecture decisions and design documents

### `deploy/`
Deployment configurations and artifacts:
- **docker/**: Dockerfiles for containerization
- **kubernetes/**: Kubernetes manifests and Helm charts for orchestration

## Setup

This project uses [uv](https://github.com/astral-sh/uv) as the package manager for fast and reliable dependency management.

### Prerequisites

- Python 3.9 or higher
- uv (install from https://github.com/astral-sh/uv)

### Installation

1. **Install uv** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Clone the repository**:
```bash
git clone https://github.com/MunchProductionz/pytorch-transformer-implementation.git
cd pytorch-transformer-implementation
```

3. **Install dependencies**:
```bash
# Install core dependencies
uv sync

# Install with development dependencies
uv sync --extra dev

# Install with notebook dependencies
uv sync --extra notebooks

# Install all optional dependencies
uv sync --all-extras
```

4. **Activate the virtual environment**:
```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

## Usage

### Training a Model

```bash
uv run python scripts/train.py --config configs/training_config.yaml
```

### Running Inference

```bash
uv run python scripts/infer.py --model-path models/checkpoint.pt --input "Your input text"
```

### Data Preprocessing

```bash
uv run python scripts/preprocess_data.py --input data/raw/ --output data/processed/
```

### Running Tests

```bash
# Run all tests
uv run pytest tests/

# Run unit tests only
uv run pytest tests/unit/

# Run with coverage report
uv run pytest tests/ --cov=pytorch_transformer --cov-report=html
```

### Code Quality

```bash
# Format code with black
uv run black src/ tests/ scripts/

# Lint code with ruff
uv run ruff check src/ tests/ scripts/

# Type checking with mypy
uv run mypy src/
```

### Using Notebooks

```bash
# Install notebook dependencies if not already installed
uv sync --extra notebooks

# Launch Jupyter Lab
uv run jupyter lab

# Or launch Jupyter Notebook
uv run jupyter notebook
```

## Development Workflow

1. **Create a feature branch**:
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** following the project structure

3. **Run tests and quality checks**:
```bash
uv run pytest tests/
uv run black src/ tests/ scripts/
uv run ruff check src/ tests/ scripts/
uv run mypy src/
```

4. **Commit and push**:
```bash
git add .
git commit -m "Description of your changes"
git push origin feature/your-feature-name
```

## Adding Dependencies

To add a new dependency:

```bash
# Add a core dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Add an optional dependency
# Edit pyproject.toml manually and run:
uv sync
```

## Project Philosophy

This project follows modern Python best practices:
- **Modular architecture**: Clear separation of concerns
- **Type hints**: Full type annotations for better code quality
- **Testing**: Comprehensive test coverage
- **Documentation**: Clear, up-to-date documentation
- **Reproducibility**: Pinned dependencies and configuration management
- **Code quality**: Automated formatting, linting, and type checking

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Ensure all tests pass and code is formatted
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
