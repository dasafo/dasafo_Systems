# 🎛️ MISSION CONTROL CENTER

> [ ⬆️ Up: [[../MOC_GLOBAL]] | 📂 Global: [[MOC_GLOBAL]] ]

## 🔴 Misiones Activas (En Progreso)
```dataview
TABLE status, agent_assigned as "Agente a Cargo", priority as "Prioridad"
WHERE type = "mission" AND status != "✅ TERMINADO"
SORT priority DESC
```

## 📝 Backlog & Cola de Espera
```dataview
TABLE priority, created_at as "Fecha Creado"
WHERE type = "mission" AND (status = "📝 BACKLOG" OR contains(status, "BACKLOG"))
SORT created_at ASC
```

## ✅ Completadas
```dataview
TABLE created_at as "Fecha Creado"
WHERE type = "mission" AND status = "✅ TERMINADO"
```
