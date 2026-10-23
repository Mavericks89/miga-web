# miga-web — web corporativa de MIGA Worldwide

Web estática (HTML + CSS) de migaworldwide.com. Objetivo: verificación de empresa en Meta Business Manager.
Los datos legales viven en `build.py` (una sola fuente); las páginas se regeneran con `python3 build.py .`.
No se editan a mano los `index.html`: se edita `build.py` y se regenera.

- Decisiones: `decisiones.md`.
- Restricciones de contenido: nada de cifras, testimonios ni logos inventados; no presentarse como asesor, bróker
  ni entidad regulada; imágenes solo propias (SVG/CSS).
