import pytest

exit_code = pytest.main(["test_unitario.py", "test_aceptacion.py"])

if exit_code == 0:
    print("✅ ¡Todos los tests pasaron correctamente! El sistema cumple los requisitos.")
else:
    print("❌ Hubo fallos en los tests. Revisá el detalle arriba.")
