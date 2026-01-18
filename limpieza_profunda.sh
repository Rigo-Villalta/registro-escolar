#!/bin/bash

echo "======================================================================"
echo "LIMPIEZA PROFUNDA Y REINICIO FORZADO"
echo "======================================================================"

echo ""
echo "1️⃣  Deteniendo servicio"
sudo systemctl stop gunicorn-registro-cedhra
sleep 2

echo ""
echo "2️⃣  Eliminando TODO el Python compilado"
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyc" -delete 2>/dev/null

echo ""
echo "3️⃣  Verificando que NO hay procesos de gunicorn corriendo"
pgrep -f "gunicorn.*registro" && echo "⚠️  Aún hay procesos!" || echo "✅ No hay procesos"

echo ""
echo "4️⃣  Forzando kill de cualquier proceso restante"
pkill -9 -f "gunicorn.*registro" 2>/dev/null
sleep 2

echo ""
echo "5️⃣  Mostrando hash de archivos modificados (para verificar que son los correctos)"
echo "   filters.py:"
md5sum personas/filters.py
echo "   admin.py:"
md5sum personas/admin.py
echo "   actions.py:"
md5sum personas/actions.py

echo ""
echo "6️⃣  Iniciando servicio limpio"
sudo systemctl start gunicorn-registro-cedhra
sleep 5

echo ""
echo "7️⃣  Verificando estado"
sudo systemctl status gunicorn-registro-cedhra --no-pager

echo ""
echo "8️⃣  Verificando que los nuevos workers están frescos"
ps aux | grep gunicorn | grep registro

echo ""
echo "======================================================================"
echo "✅ LIMPIEZA COMPLETADA"
echo "======================================================================"
echo ""
echo "Verifica los logs:"
echo "  sudo journalctl -u gunicorn-registro-cedhra -n 50"
echo ""
