#!/bin/bash

# Script para desplegar cambios en producción correctamente

echo "======================================================================"
echo "DESPLIEGUE SEGURO EN PRODUCCIÓN"
echo "======================================================================"

echo ""
echo "1️⃣  Eliminando archivos .pyc y __pycache__"
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
echo "   ✅ Archivos Python compilados eliminados"

echo ""
echo "2️⃣  Verificando cambios en filters.py"
echo "   Última modificación:"
ls -lh personas/filters.py

echo ""
echo "3️⃣  Verificando cambios en admin.py"
echo "   Última modificación:"
ls -lh personas/admin.py

echo ""
echo "4️⃣  Reiniciando SOLO el servicio gunicorn-registro-cedhra"
sudo systemctl restart gunicorn-registro-cedhra
sleep 3
echo "   ✅ Servicio reiniciado"

echo ""
echo "5️⃣  Verificando estado del servicio"
sudo systemctl status gunicorn-registro-cedhra --no-pager -l

echo ""
echo "6️⃣  Verificando procesos activos de este proyecto"
ps aux | grep gunicorn-registro-cedhra | grep -v grep

echo ""
echo "======================================================================"
echo "✅ DESPLIEGUE COMPLETADO"
echo "======================================================================"
echo ""
echo "Ahora prueba en el navegador y verifica los logs con:"
echo "  sudo journalctl -u gunicorn-registro-cedhra -f"
echo ""
