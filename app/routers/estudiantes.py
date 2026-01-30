from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter(
    prefix="/estudiantes",
    tags=["Estudiantes"]
)

# Base de datos simulada (temporal)
estudiantes_db = [
    {"id": 1, "nombre": "Juan Pérez", "matricula": "2021001", "carrera": "Ingeniería"},
    {"id": 2, "nombre": "María López", "matricula": "2021002", "carrera": "medicina"},
    {"id": 3, "nombre": "Carlos García", "matricula": "2021003", "carrera": "Derecho"},
    {"id": 4, "nombre": "Ana Martínez", "matricula": "2021004", "carrera": "Ingeniería"},
    {"id": 5, "nombre": "Pedro Sánchez", "matricula": "2021005", "carrera": "medicina"},
    {"id": 6, "nombre": "Luisa Fernández", "matricula": "2021006", "carrera": "Derecho"},
    {"id": 7, "nombre": "Jorge Ramírez", "matricula": "2021007", "carrera": "Ingeniería"},
    {"id": 8, "nombre": "Sofía Torres", "matricula": "2021008", "carrera": "medicina"},
]

@router.get("/")
def listar_estudiantes(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Cantidad de registros a retornar"),
    carrera: Optional[str] = Query(
        None,
        min_length=1,
        description="Filtrar por carrera"
    )
):
    """
    Lista todos los estudiantes con paginación y filtros opcionales.
    """

    estudiantes = estudiantes_db

    # Filtro por carrera
    if carrera:
        estudiantes = [e for e in estudiantes if e["carrera"] == carrera]

    return {
        "total": len(estudiantes),  # total correcto (filtrado)
        "skip": skip,
        "limit": limit,
        "filtros": {"carrera": carrera} if carrera else None,
        "estudiantes": estudiantes[skip: skip + limit]
    }


@router.get("/{estudiante_id}")
def obtener_estudiante(estudiante_id: int):
    """
    Obtiene un estudiante por su ID.
    """
    for estudiante in estudiantes_db:
        if estudiante["id"] == estudiante_id:
            return estudiante

    return {"error": "Estudiante no encontrado"}
