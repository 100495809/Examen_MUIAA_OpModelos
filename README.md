Se han seguido todos los comandos proporcionados:
```bash
uv init --package clasificador-paquetes
uv add pydantic scikit-learn joblib numpy scipy pytest
```

Se ha añadido lo siguiente al .toml:

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```
Y posteriormente se ha ejecutado:

```bash
uv sync
```
