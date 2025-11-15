# 📘 Developer Guide | دليل المطور

**Last Updated: 2025-11-15**  
**Version: 1.0.0**

---

## 📋 Table of Contents | جدول المحتويات

1. [Development Environment Setup](#development-environment-setup)
2. [Project Structure](#project-structure)
3. [Coding Standards](#coding-standards)
4. [Development Workflow](#development-workflow)
5. [Testing Guidelines](#testing-guidelines)
6. [Debugging](#debugging)
7. [API Development](#api-development)

---

## 🚀 Development Environment Setup

### Prerequisites | المتطلبات الأساسية

```bash
# Required Software
- Python 3.11+
- Rust 1.70+
- Docker 24.0+
- Docker Compose 2.0+
- Git 2.40+
- PostgreSQL 15+ (for local development)
- Redis 7.0+ (for local development)
```

### Initial Setup | الإعداد الأولي

```bash
# 1. Clone the repository
git clone https://github.com/Thamer-H2K/thamer-immortal-protocol.git
cd thamer-immortal-protocol

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. Install Rust dependencies
cd core
cargo build
cd ..

# 5. Setup environment variables
cp .env.example .env
nano .env  # Edit with your configuration

# 6. Initialize database
docker-compose up -d thamer-db
python scripts/init_db.py

# 7. Start development services
docker-compose up -d
```

### IDE Configuration | إعداد بيئة التطوير

#### VS Code (Recommended)
```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "rust-analyzer.cargo.loadOutDirsFromCheck": true
}
```

#### PyCharm
- Set Python interpreter to `./venv/bin/python`
- Enable Pylint and Black formatter
- Configure Rust plugin for core module

---

## 📂 Project Structure | هيكل المشروع

```
thamer-immortal-protocol/
├── api/                    # FastAPI REST API
│   ├── routes/            # API endpoints
│   ├── models/            # Pydantic models
│   ├── middleware/        # Custom middleware
│   └── requirements.txt   # API dependencies
├── core/                   # Rust performance engine
│   ├── src/              # Rust source code
│   └── Cargo.toml        # Rust dependencies
├── intelligence/          # AI/ML threat detection
│   ├── models/           # ML models
│   ├── training/         # Training scripts
│   └── requirements.txt  # ML dependencies
├── security/             # Security components
│   ├── authentication.py # JWT + MFA
│   ├── encryption.py     # AES + RSA
│   └── rate_limiter.py   # Rate limiting
├── sensors/              # Monitoring sensors
│   ├── system_monitor.py
│   └── network_monitor.py
├── response/             # Autonomous response
│   └── autonomous_response.py
├── dashboard/            # Web UI
│   ├── static/          # CSS, JS, images
│   └── templates/       # HTML templates
├── psychology_module/    # Behavioral analysis
├── tests/               # Test suite
│   ├── unit/           # Unit tests
│   ├── integration/    # Integration tests
│   └── security/       # Security tests
├── documentation/       # Complete docs
├── .github/            # GitHub workflows
├── docker-compose.yml  # Docker services
└── requirements.txt    # Global dependencies
```

---

## 📝 Coding Standards | معايير البرمجة

### Python Code Style

```python
# Use Black formatter (line length: 88)
# Use type hints for all functions
# Use docstrings (Google style)

def process_threat(
    threat_data: dict[str, Any],
    severity: int = 5,
    *,
    auto_respond: bool = True
) -> ThreatAnalysis:
    """
    Process and analyze a security threat.
    
    Args:
        threat_data: Dictionary containing threat information
        severity: Threat severity level (1-10)
        auto_respond: Whether to trigger automatic response
        
    Returns:
        ThreatAnalysis object with analysis results
        
    Raises:
        ValueError: If threat_data is invalid
        SecurityError: If threat level exceeds threshold
    """
    pass
```

### Rust Code Style

```rust
// Follow Rust standard conventions
// Use rustfmt for formatting
// Use clippy for linting

/// Process high-performance security operation
pub fn process_security_event(
    event: &SecurityEvent,
    config: &Config,
) -> Result<Response, SecurityError> {
    // Implementation
    Ok(response)
}
```

### Naming Conventions

```python
# Variables and functions: snake_case
threat_level = 5
def analyze_threat(): pass

# Classes: PascalCase
class ThreatDetector: pass

# Constants: UPPER_SNAKE_CASE
MAX_THREAT_LEVEL = 10

# Private methods: _leading_underscore
def _internal_method(): pass
```

---

## 🔄 Development Workflow | سير العمل

### Branch Strategy

```bash
main           # Production-ready code
├── develop    # Integration branch
├── feature/*  # New features
├── bugfix/*   # Bug fixes
├── hotfix/*   # Emergency fixes
└── release/*  # Release preparation
```

### Feature Development

```bash
# 1. Create feature branch
git checkout develop
git pull origin develop
git checkout -b feature/threat-prediction

# 2. Make changes and commit
git add .
git commit -m "feat: add ML-based threat prediction"

# 3. Push and create PR
git push origin feature/threat-prediction
# Create PR on GitHub: feature/threat-prediction -> develop
```

### Commit Message Format

```bash
# Format: <type>(<scope>): <subject>

feat(intelligence): add neural network for threat detection
fix(security): resolve JWT token expiration issue
docs(api): update authentication endpoint documentation
test(sensors): add unit tests for system monitor
refactor(core): optimize Rust performance engine
chore(deps): upgrade FastAPI to 0.115.5
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`

---

## 🧪 Testing Guidelines | إرشادات الاختبار

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_threat_detection.py

# Run with coverage
pytest --cov=. --cov-report=html

# Run integration tests
pytest tests/integration/ -v

# Run security tests
pytest tests/security/ -v
```

### Writing Unit Tests

```python
import pytest
from intelligence.threat_detection import ThreatDetector

class TestThreatDetector:
    @pytest.fixture
    def detector(self):
        return ThreatDetector()
    
    def test_detect_anomaly(self, detector):
        """Test anomaly detection with normal traffic"""
        data = {"requests": 100, "errors": 2}
        result = detector.detect_anomaly(data)
        assert result.is_normal is True
        assert result.confidence > 0.8
    
    def test_detect_attack(self, detector):
        """Test attack detection with malicious traffic"""
        data = {"requests": 10000, "errors": 500}
        result = detector.detect_anomaly(data)
        assert result.is_attack is True
        assert result.threat_level >= 8
```

---

## 🐛 Debugging | تصحيح الأخطاء

### Debug Mode

```bash
# Enable debug mode
export DEBUG=True
export LOG_LEVEL=DEBUG

# Run with debugger
python -m pdb main.py

# Docker debug
docker-compose -f docker-compose.yml -f docker-compose.debug.yml up
```

### Logging

```python
import logging
from core.logger import get_logger

logger = get_logger(__name__)

logger.debug("Detailed information for debugging")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error occurred", exc_info=True)
logger.critical("Critical system failure")
```

### Performance Profiling

```python
import cProfile
import pstats

# Profile function
cProfile.run('my_function()', 'profile_stats')
stats = pstats.Stats('profile_stats')
stats.sort_stats('cumulative')
stats.print_stats(20)
```

---

## 🔌 API Development | تطوير API

### Creating New Endpoint

```python
# api/routes/threats.py
from fastapi import APIRouter, Depends, HTTPException
from api.models.threat import ThreatCreate, ThreatResponse
from api.middleware.auth import get_current_user

router = APIRouter(prefix="/api/v1/threats", tags=["threats"])

@router.post("/", response_model=ThreatResponse, status_code=201)
async def create_threat(
    threat: ThreatCreate,
    current_user: User = Depends(get_current_user)
):
    """
    Create new threat entry
    
    - **name**: Threat name
    - **severity**: Severity level (1-10)
    - **description**: Detailed description
    """
    # Implementation
    return threat_response
```

### Testing API Endpoints

```bash
# Using HTTPie
http POST http://localhost:8000/api/v1/threats \
  Authorization:"Bearer $TOKEN" \
  name="SQL Injection" \
  severity:=9

# Using curl
curl -X POST http://localhost:8000/api/v1/threats \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"SQL Injection","severity":9}'
```

---

## 🛠️ Advanced Development

### Custom ML Model Integration

```python
# intelligence/models/custom_model.py
import joblib
from sklearn.base import BaseEstimator

class CustomThreatModel(BaseEstimator):
    def __init__(self, threshold=0.7):
        self.threshold = threshold
        
    def fit(self, X, y):
        # Training logic
        return self.last
        
    def predict(self, X):
        # Prediction logic
        return predictions
        
    def save(self, path: str):
        joblib.dump(self, path)
```

### Creating Custom Sensors

```python
# sensors/custom_sensor.py
from sensors.base import BaseSensor

class CustomSecuritySensor(BaseSensor):
    def __init__(self, config: dict):
        super().__init__(config)
        
    async def collect_metrics(self) -> dict:
        """Collect custom security metrics"""
        metrics = {
            "timestamp": datetime.utcnow(),
            "metric_value": self._get_metric()
        }
        return metrics
```

---

## 📚 Resources | المصادر

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Rust Book](https://doc.rust-lang.org/book/)
- [Python Best Practices](https://docs.python-guide.org/)
- [Docker Documentation](https://docs.docker.com/)

---

## 💡 Tips & Best Practices

1. **Always write tests** before pushing code
2. **Use type hints** for better code clarity
3. **Document complex logic** with comments
4. **Profile performance** for critical paths
5. **Security first** - validate all inputs
6. **Keep functions small** and focused
7. **Use async/await** for I/O operations
8. **Handle errors gracefully** with proper exception handling

---

## 📞 Support | الدعم

- **Email**: frankly.sa@gmail.com
- **GitHub Issues**: [Report Bug](https://github.com/Thamer-H2K/thamer-immortal-protocol/issues)
- **Discussions**: [Join Discussion](https://github.com/Thamer-H2K/thamer-immortal-protocol/discussions)

---

**Made with ❤️ by Thamer Aljadaan (CyberX)**  
**لا موت. لا توقف. لا استسلام.**